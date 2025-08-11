import os
from coval.conll import reader
from coval.eval import evaluator


def run_agreement(gold_file, sys_file, metrics, keep_singletons):
    metric_options = {"muc", "bcub", "ceafe", "lea"}
    doc_coref_infos = reader.get_coref_infos(gold_file, sys_file, keep_singletons=keep_singletons,
                                             NP_only=False,
                                             remove_nested=False,
                                             min_span=False)

    conll = 0
    conll_subparts_num = 0
    metrics_result = {}
    for name, metric in metrics:
        try:
            recall, precision, f1 = evaluator.evaluate_documents(doc_coref_infos,
                                                                 metric,
                                                                 beta=1)
            metrics_result[name] = {"recall": recall, "precision": precision, "f1": f1}
        except ZeroDivisionError as e:
            print(doc_coref_infos)
        if name in metric_options:
            conll += f1
            conll_subparts_num += 1

        print(name.ljust(10), "Recall: %.2f" % (recall * 100),
              " Precision: %.2f" % (precision * 100),
              " F1: %.2f" % (f1 * 100))

    if conll_subparts_num == 4:
        conll_score = (conll / 4) * 100
        print("CoNLL score: %.2f" % conll_score)
        metrics_result["conll_score"] = conll_score
    return metrics_result


def run_2_annotators_agreement(gold_files, sys_files, keep_singletons=True):
    allmetrics = [("mentions", evaluator.mentions),
                  ("muc", evaluator.muc),
                  ("bcub", evaluator.b_cubed),
                  ("ceafe", evaluator.ceafe),
                  ("lea", evaluator.lea)]
    results = []
    for gold_file, sys_file in zip(gold_files, sys_files):
        res = run_agreement(gold_file, sys_file, allmetrics, keep_singletons)
        results.append(res)
    return results


def extract_name(file_name):
    parts = file_name.split("_")
    name = "_".join(parts[-1:])
    name = name.replace(".conllu", "")
    return name


def calculate_average_scores(metrics_list, include_mentions):
    total_scores = {
        "mentions": {"recall": 0, "precision": 0, "f1": 0},
        "muc": {"recall": 0, "precision": 0, "f1": 0},
        "bcub": {"recall": 0, "precision": 0, "f1": 0},
        "ceafe": {"recall": 0, "precision": 0, "f1": 0},
        "lea": {"recall": 0, "precision": 0, "f1": 0},
    }
    counts = {
        "mentions": 0,
        "muc": 0,
        "bcub": 0,
        "ceafe": 0,
        "lea": 0,
    }
    if not include_mentions:
        total_scores.pop("mentions")
        counts.pop("mentions")
        for user_metrics in metrics_list:
            user_metrics.pop("mentions")
    
    for metrics_dict in metrics_list:
        for metric_name, metric_scores in metrics_dict.items():
            if metric_name != "conll_score":
                for score_name, score_value in metric_scores.items():
                    total_scores[metric_name][score_name] += score_value
                counts[metric_name] += 1

    for metric_name, metric_scores in total_scores.items():
        for score_name, score_value in metric_scores.items():
            total_scores[metric_name][score_name] = score_value / counts[metric_name]

    return total_scores


def find_matching_documents(list1, list2):
    import re
    doc_numbers_list1 = {}
    doc_numbers_list2 = {}
    
    for file in list1:
        match = re.search(r"/(\d+)_", file)
        if match:
            doc_numbers_list1[match.group(1)] = file
    
    for file in list2:
        match = re.search(r"/(\d+)_", file)
        if match:
            doc_numbers_list2[match.group(1)] = file

    common_docs = set(doc_numbers_list1.keys()).intersection(set(doc_numbers_list2.keys()))
    matching_files = [(doc_numbers_list1[doc], doc_numbers_list2[doc]) for doc in common_docs]
    return matching_files
