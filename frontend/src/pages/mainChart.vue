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
                color: '#353535'
            },
            textColor: '#FFFFFF'
            
        },
        autoSize: true,
        grid: {
            vertLines: { visible: false},
            horzLines: { visible: false}
        }
    })

    // the customizations for the chart
    const baseline = chart.addSeries(BaselineSeries, {
        baseValue: { type: 'price', price: 25 }, 
        topLineColor: 'rgb(58 116 203)', 
        bottomLineColor: 'rgb(255 255 255)',
        topFillColor1: 'rgb(97 123 252)',
        topFillColor2: 'rgba(255 255 255 / 0)',
        bottomFillColor1: 'rgba(186 186 186 / 0)',
        bottomFillColor2: 'rgb(255 255 255)',

  baseLineVisible: true,
  baseLineColor: 'rgba(255, 255, 255, 0.6)',
  baseLineWidth: 2,

    })

    const data = [
        { value: 1, time: '2019-04-11' }, 
        { value: 8, time: '2019-04-12' }, 
        { value: 10, time: '2019-04-13' }, 
        { value: 20, time: '2019-04-14' }, 
        { value: 3, time: '2019-04-15' }, 
        { value: 43, time: '2019-04-16' }, 
        { value: 41, time: '2019-04-17' }, 
        { value: 43, time: '2019-04-18' }, 
        { value: 56, time: '2019-04-19' }, 
        { value: 46, time: '2019-04-20' }
    ]
    baseline.setData(data)

    // fits the time and content of the chart
    chart.timeScale().fitContent()
})

</script>

<style scoped>

</style>