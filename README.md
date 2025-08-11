Hebrew Coreference Data

Contents:
- lingmess/hebrew: train/dev/test + sota_tokenized (LingMess)
- wl/hebrew: train/dev/test + head variants (WL)
- annotation/final_coref: final TNE JSON and CoNLL
- annotation/coref_pairwise/conllu_out_annotation: pairwise agreement (coref)
- annotation/mention_annotation: selected single-name annotators with large contributions

Anonymization:
- Mention annotators have been anonymized as annotator_01..annotator_08.

Coref pairwise files flattened and anonymized:
- All .conllu files moved from subfolders to annotation/coref_pairwise/
- Annotator names removed from filenames (e.g., Hadar -> _1, _2, etc.)
- Redundant conllu_out_annotation subfolder removed
