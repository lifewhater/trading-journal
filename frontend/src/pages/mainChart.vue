<template>
    <div class=" h-screen flex items-center justify-center">
        <div ref="chartContainer" class="h-[300px] w-[400px]"></div>
    </div>
</template>


<script setup lang="ts">
import { createChart, BaselineSeries } from 'lightweight-charts';
import { onMounted, ref, nextTick } from 'vue';

const chartContainer = ref<HTMLDivElement | null>(null)

// Needs async for nextTick() and chart goes in onMounted
onMounted(async () => {
    // makes sure to wait updating the DOM and then run the code
    await nextTick()
    

    console.log(chartContainer.value?.clientHeight, chartContainer.value?.clientWidth)

    // the `!` tells typescript it's a non-null value
    // the customizations for the chart
    const chart = createChart(chartContainer.value!, {
        width: chartContainer.value?.clientHeight,
        height: chartContainer.value?.clientWidth,
        layout:{
            background: {
                color: '#0f172a'
            },
            textColor: '#cbd5e1'
            
        },
        autoSize: true,
        grid: {
            vertLines: { color: 'rgba(148, 163, 184, 0.08)' },
            horzLines: { color: 'rgba(148, 163, 184, 0.08)' }
        }
    })

    // the customizations for the chart
    const baseline = chart.addSeries(BaselineSeries, {
        baseValue: { type: 'price', price: 0 }, 
          topLineColor: '#22d3ee',
          bottomLineColor: '#fb7185',
          topFillColor1: 'rgba(34, 211, 238, 0.45)',
          topFillColor2: 'rgba(34, 211, 238, 0.04)',
          bottomFillColor1: 'rgba(251, 113, 133, 0.06)',
          bottomFillColor2: 'rgba(251, 113, 133, 0.40)',

  baseLineVisible: true,
      baseLineColor: 'rgba(226, 232, 240, 0.45)',
  baseLineWidth: 2,

    })

    const backend = await fetch('http://localhost:5000/')
    const json = await backend.json()
    let running = 0
    const data = json.daily_pnl.map((row: {date: string, pnl: number}) => {
        running += row.pnl
        return { time: row.date, value: running }
    })

    baseline.setData(data)

    
})

</script>

<style scoped>

</style>