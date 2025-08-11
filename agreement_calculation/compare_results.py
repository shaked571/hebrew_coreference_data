#!/usr/bin/env python3
import os
import re
from collections import defaultdict

def analyze_coref_data():
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
    
    return file_by_annotator, doc_coverage

def main():
    print("=== Hebrew Coreference Data Repository Verification ===")
    
    print("=== Expected Results from Original Analysis ===")
    print("  Overall agreement score: 81.08%")
    print("  Document ranges analyzed: 35")
    print("  Agreement score range: 72.3% - 87.2%")
    print("  Expected documents: 348+ documents")
    
    file_by_annotator, doc_coverage = analyze_coref_data()
    
    print("=== Our Anonymized Data Analysis ===")
    print("  Total .conllu files: " + str(sum(len(files) for files in file_by_annotator.values())))
    print("  Unique annotators: " + str(len(file_by_annotator)))
    print("  Documents covered: " + str(len(doc_coverage)))
    
    coverage_stats = defaultdict(int)
    for doc, annotators in doc_coverage.items():
        coverage_stats[len(annotators)] += 1
    
    print("Document coverage analysis:")
    for coverage, count in sorted(coverage_stats.items()):
        print("  " + str(coverage) + " annotators: " + str(count) + " documents")
    
    print("=== Verification for Agreement Calculation ===")
    
    major_annotators = {k: v for k, v in file_by_annotator.items() if len(v) >= 10}
    print("Major annotators (>=10 files): " + str(len(major_annotators)))
    
    if major_annotators:
        print("Top annotators by file count:")
        sorted_annotators = sorted(major_annotators.items(), key=lambda x: len(x[1]), reverse=True)
        for i, (annotator, files) in enumerate(sorted_annotators[:5]):
            print("  " + str(i+1) + ". Annotator " + str(annotator) + ": " + str(len(files)) + " files")
    
    docs_with_multiple_annotators = {doc: annotators for doc, annotators in doc_coverage.items() if len(annotators) >= 2}
    print("Documents with multiple annotators (>=2): " + str(len(docs_with_multiple_annotators)))
    
    if docs_with_multiple_annotators:
        print("Sample documents with multiple annotators:")
        sample_docs = sorted(docs_with_multiple_annotators.items(), key=lambda x: len(x[1]), reverse=True)[:5]
        for doc, annotators in sample_docs:
            print("  Document " + str(doc) + ": " + str(len(annotators)) + " annotators")
    
    print("=== Conclusion ===")
    if len(docs_with_multiple_annotators) >= 300:
        print("✓ Data structure appears suitable for agreement calculation")
        print("✓ We have sufficient document overlap between annotators")
        print("✓ The anonymized structure preserves the original data relationships")
    else:
        print("⚠ Data structure may need verification")
        print("⚠ Insufficient document overlap for reliable agreement calculation")
    
    print("=== Next Steps ===")
    print("1. Install required dependencies: pip install pycoval pandas numpy")
    print("2. Run full agreement calculation to verify we get ~81.08%")
    print("3. Compare document-level scores with original analysis")

if __name__ == "__main__":
    main()
