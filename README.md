## Hebrew Coreference Data

Public dataset and resources for Hebrew coreference resolution. This repository provides gold-standard CoNLL-U data and accompanying inputs used by neural and LLM-based systems.

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

Notes
- The content of `data/conllu/` is sourced from the project’s gold data (“conllu_gold”) and is organized into `with_singleton` and `no_singleton` variants per split.
- `neural_input/wl` and `neural_input/lingmess` mirror the common Hebrew splits used in prior work.
- `llm_input` contains raw and tokenized documents as well as model- and LLM-derived mentions.

### Guidelines
The English guidelines for the annotation scheme are available at `guidelines/Hebrew_Coreference_Guidelines_English.pdf`.

### Citation
If you use this repository, please cite it and acknowledge the Hebrew coreference annotation effort.

### Contact
Please open an issue for questions or clarifications.
