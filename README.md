# Hebrew Coreference Data Repository

This repository contains a comprehensive dataset for Hebrew coreference resolution, including annotated data, evaluation metrics, and detailed statistics. The dataset is designed for training and evaluating coreference resolution models for Hebrew text.

## 📊 Dataset Overview

### Core Data Structure
- **lingmess/hebrew**: Train/dev/test splits + SOTA tokenized data (LingMess format)
- **wl/hebrew**: Train/dev/test splits + head variants (WL format)
- **annotation/final_coref**: Final TNE JSON and CoNLL-U annotations
- **annotation/coref_pairwise**: Pairwise agreement annotations (coreference)
- **annotation/mention_annotation**: Single-name annotators with large contributions

## 📈 Dataset Statistics

### Overall Dataset Composition
- **Total Documents**: 351 (301 train, 26 dev, 24 test)

### Text Statistics
- **Total Sentences**: 6,151
- **Total Tokens**: 159,975
- **Average Sentences per Document**: 17.52
- **Average Tokens per Document**: 455.77
- **Median Sentences per Document**: 16.0
- **Median Tokens per Document**: 386.0

## 🏷️ Mention Statistics

### Overall Mention Counts
- **Total Mentions (no singleton)**: 19,483
- **Total Mentions (with singleton)**: 45,689
- **Singleton Mentions**: 26,206 (57.4%)
- **Unique Mentions**: 29,755

### Mention Distribution by Split
- **Train**: 16,907 mentions
- **Dev**: 1,181 mentions  
- **Test**: 1,395 mentions

### Mention Characteristics
- **Average Mention Length**: 14.58 tokens
- **Median Mention Length**: 10.0 tokens
- **Min Mention Length**: 1 token
- **Max Mention Length**: 260 tokens
- **Average Mention Span**: 14.67 tokens

### Top Mention Types
1. **הוא** (he) - 2,618 occurrences
2. **הם** (they) - 1,079 occurrences
3. **היא** (she) - 1,044 occurrences
4. **אני** (I) - 298 occurrences
5. **זה** (this) - 254 occurrences
6. **הן** (they-fem) - 238 occurrences
7. **כך** (thus) - 206 occurrences
8. **אנחנו** (we) - 205 occurrences
9. **ישראל** (Israel) - 175 occurrences
10. **מה** (what) - 152 occurrences

## 🤝 Agreement Analysis

### Coreference Agreement Scores
- **Final Overall**: CoNLL Score: 0.811, Mention Score: 0.850

### Final Agreement Scores
- **Coreference Agreement**: 81.1%
- **Mention Agreement**: 85.0%
- 
## 📁 Repository Structure

```
hebrew_coreference_data/
├── lingmess/hebrew/           # LingMess format data
│   ├── train.hebrew.jsonlines
│   ├── dev.hebrew.jsonlines
│   ├── test.hebrew.jsonlines
│   └── sota_tokenized/
├── wl/hebrew/                 # WL format data
│   ├── train.hebrew.jsonlines
│   ├── dev.hebrew.jsonlines
│   ├── test.hebrew.jsonlines
│   └── *_head.hebrew.jsonlines
├── annotation/                # Annotation data
│   ├── final_coref/          # Final consolidated annotations
│   │   ├── conllu/           # CoNLL-U format
│   │   └── tne/              # TNE JSON format
│   ├── coref_pairwise/       # Pairwise agreement annotations
│   └── mention_annotation/   # Individual annotator data
│       ├── annotator_01/     # Anonymized annotator data
│       ├── annotator_02/
│       └── ...               # (8 total annotators)
├── agreement_calculation/     # Agreement calculation tools
└── statistics/                # Comprehensive data statistics
    ├── outputs/               # Generated statistics and visualizations
    ├── data_statistics.py     # Basic dataset analysis
    ├── agreement_analysis.py  # Agreement analysis
    ├── comprehensive_statistics.py # Complete analysis
    └── tne_mention_statistics.py  # TNE mention analysis
```

## 🔒 Anonymization

- **Mention annotators** have been anonymized as `annotator_01` through `annotator_08`
- **Coreference pairwise files** have been flattened and anonymized
- All `.conllu` files moved from subfolders to `annotation/coref_pairwise/`
- Annotator names removed from filenames (e.g., John → _1, _2, etc.)
- Redundant `conllu_out_annotation` subfolder removed

## 📊 Statistical Analysis Tools

The repository includes comprehensive statistical analysis tools in the `statistics/` directory:

### Available Scripts
- **`data_statistics.py`**: Basic dataset statistics and visualizations
- **`agreement_analysis.py`**: Detailed agreement analysis and scores
- **`comprehensive_statistics.py`**: Complete dataset and agreement analysis
- **`tne_mention_statistics.py`**: TNE mention statistics and analysis
- **`conllu_mention_counter.py`**: CONLL-U mention counting and comparison

### Generated Outputs
- **JSON files**: Detailed statistics in structured format
- **PNG files**: Visualizations showing trends and distributions
- **Console output**: Formatted statistics summary

## 🚀 Usage

### Basic Dataset Access
```python
# Access LingMess format data
from lingmess.hebrew import load_data
train_data = load_data("train.hebrew.jsonlines")

# Access WL format data  
from wl.hebrew import load_data
dev_data = load_data("dev.hebrew.jsonlines")
```

### Running Statistics
```bash
# Basic dataset analysis
python statistics/data_statistics.py

# Agreement analysis
python statistics/agreement_analysis.py

# Complete analysis
python statistics/comprehensive_statistics.py
```

## 📋 Requirements

The statistical analysis tools require:
- pandas
- numpy  
- matplotlib
- seaborn

Install with:
```bash
pip install pandas numpy matplotlib seaborn
```

## 📄 Data Formats

### LingMess Format
- JSONLines format with tokenized text and annotations
- Includes sentence boundaries and token information
- Compatible with modern NLP pipelines

### WL Format
- Alternative format with head variant annotations
- Provides different annotation perspectives
- Useful for comparative analysis

### CoNLL-U Format
- Standard format for dependency and coreference annotations
- Includes morphological and syntactic information
- Widely supported by NLP tools

### TNE Format
- Custom JSON format for mention annotations
- Rich metadata about mention types and positions
- Includes sentence position distributions

## 🤝 Contributing

This dataset represents collaborative work from multiple annotators and researchers. The repository maintains anonymized versions of annotations while preserving the quality and structure of the data.

## 📚 Citation

If you use this dataset in your research, please cite the original work and acknowledge the collaborative annotation effort.

## 📞 Contact

For questions about the dataset or statistical analysis tools, please refer to the repository issues or contact the maintainers.

---

*This README was generated based on comprehensive statistical analysis of the Hebrew coreference dataset. All statistics are derived from actual data analysis and represent the current state of the repository.*
