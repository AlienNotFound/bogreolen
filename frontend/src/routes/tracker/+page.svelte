<script lang="ts">	
	import type { PageData } from './$types';
	import { trackerCalendarCells } from '$lib/utils/date';
	let { data }: { data: PageData } = $props();
	const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

	const calendarCells = trackerCalendarCells();
	const trackDates: (Date | null)[] = []
	
	data.tracks.forEach(date => {
		const convertedDate = new Date(date.date)
		trackDates.push(convertedDate);
	});
</script>

<h1>Tracker</h1>

<div id="trackerCalendar">
	{#each days as day}
	<div class="grid">
		<h2>{day}</h2>
	</div>
	{/each}

	{#each calendarCells as cell}
		<div class="grid">
			<p>
				{cell?.getDate()}
			</p>

			{#if cell?.toDateString() == trackDates[0]?.toDateString()}
				{data.tracks[cell!.getDate()].title}
			{/if}
		</div>
		
	{/each}
</div>

<style>
	#trackerCalendar {
		width: 70vh;
		height: 60vh;
		display: grid;
		grid-template-columns: repeat(7, 1fr);
		grid-template-rows: 8% repeat(5, 1fr);
		background-color: #000;
		border: 1px solid #000;
		aspect-ratio: 1;
		gap: 1px;

	}

	.grid {
		background-color: aliceblue;
	}
</style>