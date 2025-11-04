<script lang="ts">	
	import type { PageData } from './$types';
	import { trackerCalendarCells } from '$lib/utils/date';
	import Trackermodal from '$lib/components/trackermodal.svelte';
	let { data }: { data: PageData } = $props();
	const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
	const currentMonth: string = new Date().toLocaleString('default', { month: "long"});
    let showModal = $state(false);
	let selectedDate: string = $state("");
	let newModalInfo: Track | null = $state(null);
	
	const calendarCells = trackerCalendarCells();
	const trackDates: (Date | null)[] = []
	
	data.tracks.forEach(date => {
		const convertedDate = new Date(date.date)
		trackDates.push(convertedDate);
	});
	
	function toggleModal(info: Track | null, date: string) {
		newModalInfo = info,
		selectedDate = date;
		showModal = !showModal;
    }
</script>

<svelte:head>
  <title>Tracker</title>
</svelte:head>

{#if showModal}
<Trackermodal
modalInfo={newModalInfo}
selectedDate={selectedDate}
bind:showModal={showModal} />
{/if}

<div id="calendarWrapper">
	<h1>Tracker - {currentMonth}</h1>
	<div id="trackerCalendar">
		{#each days as day}
		<div class="grid">
			<h2>{day}</h2>
		</div>
		{/each}
		
		{#each calendarCells as cell}
			<div class="grid">
				<p>{cell?.getDate()}</p>
				
				{#each trackDates as dates, i}
					{#if cell?.toDateString() == dates?.toDateString()}
						<button class="gridButton" onclick={() => toggleModal(data.tracks[i], cell?.toDateString())}>
							{data.tracks[i].title}					
						</button>
					{/if}
				{/each}
			</div>
		{/each}
	</div>
</div>

<style>

	#calendarWrapper {
		display: grid;
		justify-content: center;
		flex-direction: column;
	}
	#trackerCalendar {
		width: 80vh;
		height: 60vh;
		display: grid;
		grid-template-columns: repeat(7, 1fr);
		grid-template-rows: 8% repeat(5, 1fr);
		background-color: rgb(163, 175, 121);
		border: 1px solid #e9edc9ff;
		border-radius: 5px;
		aspect-ratio: 1;
		gap: 1px;
	}
	
	.grid {
		padding: 5%;
	}
	.grid, .gridButton {
		background-color: #e9edc9ff;
	}

	.gridButton {
		border-radius: 5px;
		padding: 2%;
  		font-size: 1em;
		text-align: left;
		font-weight: 400;
		display: flex;
		flex-direction: column;
	}

	.gridButton:hover {
		background-color: #ccd5aeff;
	}
</style>