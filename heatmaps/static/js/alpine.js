document.addEventListener('alpine:init', () => {
    Alpine.data('heatmap', () => ({
        timeframe: 'daily',
        loading: false,

        async changeTimeframe(newTimeframe) {
            this.loading = true;
            this.timeframe = newTimeframe;

            try {
                const response = await fetch(`/heatmap/${newTimeframe}/`);
                const data = await response.json();
                // Update heatmap data here
            } catch (error) {
                console.error('Error fetching heatmap data:', error);
            } finally {
                this.loading = false;
            }
        }
    }));
});
