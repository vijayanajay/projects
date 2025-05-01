def export_results_to_csv(results):
    keys = list(results.keys())
    values = [str(results[k]) for k in keys]
    header = ','.join(keys)
    row = ','.join(values)
    return f"{header}\n{row}" 