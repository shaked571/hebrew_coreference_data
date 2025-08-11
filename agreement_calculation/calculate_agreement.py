#!/usr/bin/env python3
import os
import re
from collections import defaultdict
import pandas as pd
import numpy as np
from agreement_utils import (
    extract_name, run_2_annotators_agreement, calculate_average_scores,
    find_matching_documents
)


def extract_document_number(file_path):
    match = re.search(r"/(\d+)_", file_path)
    if match:
        return match.group(1)
    return None


def main():
    print("=== Coreference Agreement Calculation ===")
    print("Using anonymized data structure...")
    
    conllu_annotated_files_path = "../annotation/coref_pairwise"
    keep_singletons = False
    calc_with_mentions = False
    
    file_by_annotator = defaultdict(list)
    
    for file in os.listdir(conllu_annotated_files_path):
        if file.endswith(".conllu"):
            annotator_id = extract_name(file)
            if annotator_id:
                file_by_annotator[annotator_id].append(file)
    
    print(f"Found {len(file_by_annotator)} annotators")
    for annotator, files in file_by_annotator.items():
        print(f"  {annotator}: {len(files)} files")
    
    scores = defaultdict(list)
    docs_agreement_score = {}
    
    annotator_names = list(file_by_annotator.keys())
    
    if len(annotator_names) < 2:
        print("Need at least 2 annotators for agreement calculation")
        return
    
    print(f"
Calculating agreement between {len(annotator_names)} annotators...")
    
    # Calculate pairwise agreement
    for i, name1 in enumerate(annotator_names):
        for j, name2 in enumerate(annotator_names[i + 1:], i + 1):
            a1_f = []
            a2_f = []

            for key, a1_file in file_by_annotator[name1].items():
                if key in file_by_annotator[name2]:
                    a1_f.append(os.path.join(conllu_annotated_files_path, a1_file))
                    a2_f.append(os.path.join(conllu_annotated_files_path, file_by_annotator[name2][key]))

            print(f"name1: {name1}")
            print(f"name2: {name2}")
            print(f"Number of file couples: {len(a1_f)}")
            
            common = find_matching_documents(a1_f, a2_f)
            print(f"Found {len(common)} matching document pairs")
            
            for a1_f, a2_f in common:
                try:
                    doc_id = extract_document_number(a1_f)
                    if doc_id:
                        score = calculate_average_scores(
                            run_2_annotators_agreement([a1_f], [a2_f], keep_singletons), 
                            calc_with_mentions
                        )
                        scores[doc_id].append(score)
                        print(f"Document {doc_id}: Agreement calculated successfully")
                except Exception as e:
                    print(f"Error in {a1_f} and {a2_f}: {e}")
                    continue
    
    print("
=== Agreement Results ===")
    
    for doc, data in scores.items():
        if data:
            f1_scores = {
                "bcub": [d["bcub"]["f1"] for d in data if "bcub" in d],
                "ceafe": [d["ceafe"]["f1"] for d in data if "ceafe" in d],
                "lea": [d["lea"]["f1"] for d in data if "lea" in d],
                "muc": [d["muc"]["f1"] for d in data if "muc" in d]
            }
            
            avg_f1_scores = {}
            for metric, scores_list in f1_scores.items():
                if scores_list:
                    avg_f1_scores[metric] = np.mean(scores_list)
                else:
                    avg_f1_scores[metric] = 0.0
            
            if avg_f1_scores:
                overall_doc_score = np.mean(list(avg_f1_scores.values()))
                docs_agreement_score[doc] = overall_doc_score
                print(f"Document {doc}: {overall_doc_score:.4f}")
    
    if docs_agreement_score:
        overall_agreement = sum(docs_agreement_score.values()) / len(docs_agreement_score) * 100
        print(f"
=== Final Results ===")
        print(f"Overall agreement score: {overall_agreement:.2f}%")
        print(f"Number of documents processed: {len(docs_agreement_score)}")
        
        print(f"
Document-level agreement scores:")
        for doc in sorted(docs_agreement_score.keys(), key=lambda x: int(x) if x.isdigit() else 0):
            score = docs_agreement_score[doc] * 100
            print(f"  Document {doc}: {score:.2f}%")
        
        scores_list = list(docs_agreement_score.values())
        print(f"
Summary Statistics:")
        print(f"  Mean: {np.mean(scores_list) * 100:.2f}%")
        print(f"  Mean: {np.mean(scores_list) * 100:.2f}%")
        print(f"  Median: {np.median(scores_list) * 100:.2f}%")
        print(f"  Std: {np.std(scores_list) * 100:.2f}%")
        print(f"  Min: {np.min(scores_list) * 100:.2f}%")
        print(f"  Max: {np.max(scores_list) * 100:.2f}%")
        
        return overall_agreement
    else:
        print("No valid agreement scores calculated")
        return None


if __name__ == "__main__":
    main()
