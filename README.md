## Hebrew Coreference Data

Public dataset and resources for Hebrew coreference resolution. This repository provides gold-standard CoNLL-U data and accompanying inputs used by neural and LLM-based systems.

### Dataset Overview

- **Total Documents**: 351 (301 train, 26 dev, 24 test)
- **Total Sentences**: 6,151
- **Total Tokens**: 159,975

### Mention Statistics

- **Total Mentions (no singleton)**: 19,483
- **Total Mentions (with singleton)**: 45,689
- **Singleton Mentions**: 26,206 (57.4%)

#### Distribution across splits:
- **Train**: 16,907 mentions
- **Dev**: 1,181 mentions  
- **Test**: 1,395 mentions

### Agreement Scores

- **Coreference Agreement**: CoNLL Score: 0.811, Mention Score: 0.850

### Data layout

```
data/
├── conllu/                    # Gold CoNLL-U splits
│   ├── no_singleton/          # train/dev/test without singletons
│   └── with_singleton/        # train/dev/test with singletons
├── neural_input/              # Inputs for neural models
│   ├── wl/                    # WL format (train/dev/test + head variants)
│   └── lingmess/              # LingMess format (train/dev/test; SOTA tokenized)
└── llm_input/                 # Inputs and outputs used with LLM pipelines
    ├── mentions_by_llm_from_raw/
    ├── mentions_by_model_danit_parse/
    ├── mentions_by_model_gold_parse/
    ├── raw_documents/
    ├── tokenized_documents/
    └── tokenized_documents_danit_tokenization/
```

### Repository Structure

```
hebrew_coreference_data/
├── data/                      # Main data directory
│   ├── conllu/               # Gold standard CoNLL-U annotations
│   ├── neural_input/         # Neural model inputs
│   └── llm_input/            # LLM pipeline data
├── guidelines/                # Annotation guidelines
├── agreement_calculation/     # Agreement calculation tools
└── annotation/                # Original annotation data
    ├── final_coref/          # Final consolidated annotations
    ├── coref_pairwise/       # Pairwise agreement annotations
    └── mention_annotation/   # Individual annotator data
```

Notes
- The content of `data/conllu/` is sourced from the project's gold data ("conllu_gold") and is organized into `with_singleton` and `no_singleton` variants per split.
- `neural_input/wl` and `neural_input/lingmess` mirror the common Hebrew splits used in prior work.
- `llm_input` contains raw and tokenized documents as well as model- and LLM-derived mentions.

### Guidelines
The English guidelines for the annotation scheme are available at `guidelines/Hebrew_Coreference_Guidelines_English.pdf`.

### Citation
If you use this repository, please cite it and acknowledge the Hebrew coreference annotation effort.

### Contact
Please open an issue for questions or clarifications.
