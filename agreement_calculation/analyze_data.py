#!/usr/bin/env python3
import os
import re
from collections import defaultdict

def analyze_coref_data():
    print("=== Coreference Data Analysis ===")
    print("Analyzing anonymized data structure...")
    
    conllu_annotated_files_path = "../annotation/coref_pairwise"
    
    if not os.path.exists(conllu_annotated_files_path):
        print("Path not found: " + conllu_annotated_files_path)
        return
    
    all_files = [f for f in os.listdir(conllu_annotated_files_path) if f.endswith(".conllu")]
    print("Total .conllu files found: " + str(len(all_files)))
    
    file_by_annotator = defaultdict(list)
    doc_coverage = defaultdict(set)
    
    for file in all_files:
        parts = file.split("_")
        if len(parts) >= 2:
            annotator_id = parts[-1].replace(".conllu", "")
            if annotator_id.isdigit():
                file_by_annotator[annotator_id].append(file)
                
                doc_match = re.search(r"(\d+)_", file)
                if doc_match:
                    doc_num = doc_match.group(1)
                    doc_coverage[doc_num].add(annotator_id)
    
    print("Found " + str(len(file_by_annotator)) + " annotators:")
    for annotator, files in sorted(file_by_annotator.items(), key=lambda x: int(x[0])):
        print("  Annotator " + str(annotator) + ": " + str(len(files)) + " files")
    
    print("Document coverage analysis:")
    print("Total unique documents: " + str(len(doc_coverage)))
    
    coverage_stats = defaultdict(int)
    for doc, annotators in doc_coverage.items():
        coverage_stats[len(annotators)] += 1
    
    print("Documents by annotator coverage:")
    for coverage, count in sorted(coverage_stats.items()):
        print("  " + str(coverage) + " annotators: " + str(count) + " documents")
    
    return file_by_annotator, doc_coverage

def main():
    print("=== Hebrew Coreference Data Repository Analysis ===")
    file_by_annotator, doc_coverage = analyze_coref_data()
    
    print("=== Summary ===")
    print("Coreference annotators: " + str(len(file_by_annotator)))
    print("Documents covered: " + str(len(doc_coverage)))
    
    if file_by_annotator:
        total_files = sum(len(files) for files in file_by_annotator.values())
        print("Total .conllu files: " + str(total_files))
        avg_files = total_files / len(file_by_annotator)
        print("Average files per annotator: " + str(avg_files))

if __name__ == "__main__":
    main()
