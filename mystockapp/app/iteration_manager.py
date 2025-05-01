class IterationWorkflowManager:
    def run_iteration(self, fwt_results, config):
        for i, metrics in enumerate(fwt_results):
            if (
                metrics['avg_return_per_trade'] >= config['target_return_pct'] and
                metrics['consistency_score'] >= config['consistency_score_threshold']
            ):
                return i
        return None 