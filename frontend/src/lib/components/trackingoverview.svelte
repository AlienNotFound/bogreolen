<script lang="ts">
    import { onMount } from "svelte";
    import { fetchGetRequestById, fetchPostRequest } from "$lib/api/common";
    import { getCurrentWeek, matchTrackToDate } from "$lib/utils/date";

    let tracks = $state<Track[]>([]);
    let modalInfo = $state<Book[]>([]);
    let showModal = $state(false)
    let loading = $state(true);
    let week = $state(getCurrentWeek());
    let error_message = $state();
    let formData: Record<number, {current_page: number, last_page: number, error_message: string}> = {};

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
        const data = formData[book_id];
        try {
            if (!data.current_page || !data.last_page) {
                return;
            }

            if(data.current_page > data.last_page) {
                data.error_message = "Current page cannot be higher than last page."
                return;
            }
            await fetchPostRequest('track/' + book_id,
                {
                    "read_today": true,
                    "current_page": data.current_page,
                    "last_page": data.last_page
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

    function updateField(book_id: number, field: 'current_page' | 'last_page', value: number) {
		if (!formData[book_id]) {
			formData[book_id] = {current_page: 0, last_page: 0, error_message: ''};
		}
		formData[book_id][field] = value;
	}

    function openModal() {
    modalInfo.forEach(book => {
        if (!formData[book.book_id]) {
            formData[book.book_id] = {current_page: 0, last_page: 0, error_message: ''};
        }
    });
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
                {#each matchTrackToDate(day.raw_date, tracks) as track}
                <p>{track.title}</p>
                {/each}
                <button onclick={() => openModal()}
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
            {#each modalFilter(modalInfo) as info}
            <div class="books">
                <h3>{info.title}</h3>
                <img src={info.image} alt="">
                
                <form onsubmit={() => markAsRead(info.book_id)}>
                    <h4>Current page:</h4>
                    <input type="number"
                    value={formData[info.book_id].current_page ?? ''} 
                    oninput={(e) => updateField(info.book_id, 'current_page', +e.currentTarget.value)}
                    required>
                    <h4>Last page:</h4>
                    <input type="number"
                    value={formData[info.book_id].last_page ?? ''}
                    oninput={(e) => updateField(info.book_id, 'last_page', +e.currentTarget.value)}>
                    {#if error_message}
                    <p class="error">{error_message}</p>
                    {/if}
                    <button>Mark as read</button>
                </form>            
            </div>
            {/each}
            <button id="modalClose" onclick={() => showModal = !showModal}>X</button>
        </div>
    </div>
{/if}

<style>
    #trackingOverviewBar,
    .trackCard,
    .trackList,
    #modalWrapper,
    .modal,
    .books {
        display: flex;
    }
    
    #trackingOverviewBar,
    .books {
        justify-content: space-between;
    }

    .error {
        color: rgb(173, 46, 23);
    }
    
    .trackCard {
        flex-direction: column;
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
        height: 60vh;
        padding: 2% 3%;
    }

    #modalClose {
        height: 6vh;
    }

    .books {
        flex-direction: column;
        padding: 2% 3%;
    }

    .books img {
        object-fit: contain;
    }

    .books input {
        -moz-appearance: textfield;
        appearance: textfield;
    }

    input::-webkit-outer-spin-button,
    input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
    }
</style>