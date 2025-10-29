<script lang="ts">
    import { onMount } from "svelte";
    import { fetchGetRequestById, fetchPostRequest } from "$lib/api/common";
    import { getCurrentWeek, matchTrackToDate } from "$lib/utils/date";

    let tracks = $state<Track[]>([]);
    let modalInfo = $state<Book[]>([]);
    let showModal = $state(false)
    let loading = $state(true);
    let week = $state(getCurrentWeek());
    let current_page = $state();
    let last_page = $state();

    async function fetchTracks() {
        try {
            tracks = await fetchGetRequestById<Track[]>('tracks/user/', '1');          
        } catch (error) {
            console.error(error);
        } finally {
            loading = false;
        }
    }
    
    async function fetchModalInfo() {
        try {
            modalInfo = await fetchGetRequestById('tracks/modal/user/', '1')
        } catch (err) {
            console.error(err);
        } finally {
            loading = false;
        }        
    }

    async function markAsRead(book_id: number) {
        try {
            await fetchPostRequest('track/' + book_id,
                {
                    "read_today": true,
                    "current_page": current_page,
                    "last_page": last_page
                }
            )
            showModal = false;
        } catch (err) {
            console.error(err);
        }
    }

    onMount(async () => {
        await Promise.all([fetchTracks(), fetchModalInfo()]);
        loading = false;
    });

    function modalFilter(tracks: Book[]): Book[] {
        const result = tracks
                        .filter(t => t.book_status === "Reading" || t.book_status === "Want to read")
                        .map(t => ({book_id: t.book_id, title: t.title, image: t.image, book_status: t.book_status}));
        return result
    }
</script>

<div>
    {#if loading}
        <div>loading..</div>
    {:else}
        {#each week as day}
        <div class="trackCard {day.isToday ? 'today' : ''}">
            <h3>{day.name} {day.date}</h3>
            <div class="trackList">
                <p>Books you've read:</p>
                {#each matchTrackToDate(day.raw_date, tracks) as track}
                <p>{track.title}</p>
                {/each}
                <button onclick={() => (showModal = !showModal)}
                        style="display: {day.isToday ? 'inline' : 'none'};
                                width: 100%;
                                margin-top: 10px">Read today</button>
            </div>
        </div>
        {/each}
    {/if}
</div>

{#if showModal}
    <div class="modal">
        {#each modalFilter(modalInfo) as info}
        <div class="books">
            <p>{info.title}</p>
            <img src={info.image} alt="">
            <h4>Current page:</h4>
            <input type="text" bind:value={current_page}>
            <h4>Last page:</h4>
            <input type="text" bind:value={last_page}>
            <button onclick={() => markAsRead(info.book_id)}>Mark as read</button>
        </div>
        {/each}
    </div>
{/if}

<style>
    div {
        display: flex;
        justify-content: space-between;
    }
    
    .trackCard {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 2%;
        /* border: 1px #000 solid; */
    }

    .trackCard.today {
        background-color: #e9edc9;
        box-shadow:  0px 0px 5px 4px #e9edc9 ;
    }

    .trackList {
        display: flex;
        flex-direction: column;
        align-items: start;
        justify-content: flex-start;
        height: 100%;
    }

    .books {
        flex-direction: column;
    }
</style>