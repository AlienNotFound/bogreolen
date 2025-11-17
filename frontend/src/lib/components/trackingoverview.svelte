<script lang="ts">
    import { onMount } from "svelte";
    import { getCurrentWeek, matchTrackToDate } from "$lib/utils/date";
    import type { ActionData } from "../../routes/$types";
    import { enhance } from "$app/forms";

    let { tracks, modalInfo, form }: {tracks: Track[], modalInfo: TrackModal[], form: ActionData } = $props();
    let showModal = $state(false)
    let loading = $state(true);
    let week = $state(getCurrentWeek());
    let error_message = $state();
    let formData: Record<number, {current_page: number, last_page: number, error_message: string}> = {};

    onMount(async () => {
        loading = false;
    });

    function modalFilter(tracks: TrackModal[]): TrackModal[] {
        if (tracks.length > 0) {
            const result = tracks
                            .filter(t => t.listname === "Reading" || t.listname === "Want to read")
                            .map(t => ({track_id: t.track_id, book_id: t.book_id, title: t.title, image: t.image, listname: t.listname, current_page: t.current_page, last_page: t.last_page}));
            return result
        }
        return []
    }

    function updateField(book_id: number, field: 'current_page' | 'last_page', value: number) {
		if (!formData[book_id]) {
			formData[book_id] = {current_page: 0, last_page: 0, error_message: ''};
		}
		formData[book_id][field] = value;
	}

    function toggleModal() {
        showModal = !showModal;

        if (showModal) {
            document.body.style.overflow = "hidden";
        } else {
            document.body.style.overflow = "scroll";

        }
    }
</script>

<div id="trackingOverviewBar">
    {#if loading}
        <div>loading..</div>
    {:else}
        {#each week as day}
        <div class="trackCard {day.isToday ? 'today' : ''}">
            <h3>{day.name} {day.date}</h3>
            <div class="trackList">
                <p>Books you've read:</p>
                {#if tracks.length > 0}
                    {#each matchTrackToDate(day.raw_date, tracks) as track}
                        <p>{track.title}</p>
                    {/each}
                {/if}
                <button onclick={() => toggleModal()}
                        style="display: {day.isToday ? 'inline' : 'none'};
                                width: 100%;
                                margin-top: 10px">Read today</button>
            </div>
        </div>
        {/each}
    {/if}
</div>

{#if showModal}
    <div id="modalWrapper">
        <div class="modal">
            <div id="modalHeader">
                <button id="modalClose" onclick={() => toggleModal()}>X</button>
            </div>
            <div id="bookList">
                {#if modalInfo}
                    {#each modalFilter(modalInfo) as info}
                    <div class="books">
                        <h3>{info.title}</h3>
                        <img src={info.image} alt="">
                    
                        <form id="pagesForm" method="POST" action="?/track_book" use:enhance={() => {
                                                            return async ({ update }) => {
                                                                update({ reset: false });
                                                            }
                                                            }}>
                            <input type="text" name="book_id" value={info.book_id} hidden>
                            <h4>Current page:</h4>
                            <input type="number"
                            name="current_page"
                            value={info.current_page ?? 0} 
                            oninput={(e) => updateField(info.book_id, 'current_page', +e.currentTarget.value)}
                            required>
                            
                            <h4>Last page:</h4>
                            <input type="number"
                            name="last_page"
                            value={info.last_page ?? ''}
                            oninput={(e) => updateField(info.book_id, 'last_page', +e.currentTarget.value)}>
                            {#if error_message}
                            <p class="error">{error_message}</p>
                            {/if}
                            <button>Mark as read</button>
                        </form>            
                    </div>
                    {/each}
                {/if}

            </div>
            {#if form?.error}
                <div class="error">
                    <p>{form?.error}</p>
                </div>
            {/if}
        </div>
    </div>
{/if}

<style>
    #trackingOverviewBar,
    .trackCard,
    .trackList,
    #modalWrapper,
    #modalHeader,
    .modal,
    #bookList,
    .books {
        display: flex;
    }
    
    #trackingOverviewBar,
    .books {
        justify-content: space-between;
    }

    .trackCard,
    .modal {
        flex-direction: column;
    }

    .error {
        color: rgb(173, 46, 23);
    }
    
    .trackCard {
        align-items: center;
        padding: 2%;
    }

    .trackCard.today {
        background-color: #e9edc9;
        box-shadow:  0px 0px 5px 4px #e9edc9 ;
    }

    .trackList {
        flex-direction: column;
        align-items: start;
        justify-content: flex-start;
        height: 100%;
    }

    #trackingOverviewBar {
        padding: 1% 0;
    }

    #modalWrapper {
        position: absolute;
        top: 0;
        left: 0;
        justify-content: center;
        align-items: center;
        width: 100vw;
        height: 100vh;
        background-color: #0000003b;
    }

    .modal {
		background-color: #ccd5ae;
        height: 64vh;
        width: 55vw;
        padding: 2% 3%;
    }
    
    #bookList {
        overflow-x: scroll;
        overflow-y: hidden;      
        flex-direction: row;  
    }

    #modalHeader {
        align-self: end;
    }
    #modalClose {
        height: 4vh;
    }

    .books {
        min-width: 15vw;
        max-width: 15vw;
        flex-direction: column;
        padding: 1% 3% 2% 3%;
    }

    .books img {
        max-width: 100%;
        object-fit: contain;
        margin-bottom: 4%;
    }

    .books input {
        -moz-appearance: textfield;
        appearance: textfield;
        margin-bottom: 2%;
    }

    #pagesForm {
        display: flex;
        flex-direction: column;
    }
</style>