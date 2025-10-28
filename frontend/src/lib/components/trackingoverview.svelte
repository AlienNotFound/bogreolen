<script lang="ts">
    import { json } from "@sveltejs/kit";
    import { onMount } from "svelte";

    type Day = {
        name: string;
        date: string;
        raw_date: Date;
        isToday: boolean;
    };

    type Track = {
        book_id: number,
        title: string,
        book_status: string,
        date: string
    }

    type Book = {
        book_id: number,
        title: string,
        image: string,
        book_status: string
    }

    let tracks = $state<Track[]>([]);
    let modalInfo = $state<Book[]>([]);
    let showModal = $state(false)
    let loading = $state(true);
    let week = $state(getCurrentWeek());
    let current_page = $state();
    let last_page = $state();

    function getCurrentWeek() {
        const today = new Date();

        const firstDayOfWeek = new Date(today);
        const day = today.getDay();
        const diff = (day === 0 ? -6 : 1) - day;
        firstDayOfWeek.setDate(today.getDate() + diff);

        const days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
        const result: Day[] = [];

        for (let i = 0; i < 7; i++) {
        const d = new Date(firstDayOfWeek);
        d.setDate(firstDayOfWeek.getDate() + i);

        result.push({
            name: days[i],
            date: d.toLocaleDateString("en-US", { month: "short", day: "numeric" }),
            raw_date: d,
            isToday:
            d.toDateString() === today.toDateString(),
            });
        }

        return result;
    }

    async function fetchTracks() {
        try {
            const response = await fetch('http://localhost:8000/tracks/user/1')
            tracks = await response.json();
            console.log(tracks);
        } catch (err) {
            console.error(err);
        } finally {
            loading = false;
        }
    }
    
    async function fetchModalInfo() {
        try {
            const response = await fetch('http://localhost:8000/tracks/modal/user/1')
            modalInfo = await response.json();
            console.log(modalInfo);
        } catch (err) {
            console.error(err);
        } finally {
            loading = false;
        }        
    }

    async function markAsRead(book_id: number) {
        try {
            const response = await fetch('http://localhost:8000/track/' + book_id, {
                method: 'POST',
                body: JSON.stringify({
                    "read_today": true,
                    "current_page": current_page,
                    "last_page": last_page
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            const result = await response.json();
            // console.log(result);
        } catch (err) {
            console.error(err);
        } finally {
            loading = false;
        }  
    }

    onMount(() => {
        fetchTracks();
        fetchModalInfo();
    });

    function formatDate(d: any) {
        return new Date(d).toISOString().split('T')[0];
    }

    function matchTrackToDate(day: any) {
        const seen = new Map();
        return tracks.filter(t => 
            formatDate(t.date) === formatDate(day)
        ).filter(t => {
            if (seen.has(t.book_id)) return false;
            seen.set(t.book_id, true)
            return true;
        })
    }

    function modalFilter(tracks: any) {
        const result = Array.from(tracks.map(t => (t.book_status == "Reading" || t.book_status == "Want to read") && {book_id: t.book_id, title: t.title, image: t.image}))
                            .filter(Boolean);
        console.log(result)
        return result
    }


</script>

<div>
    {#if loading}
        <div>loading..</div>
    {:else}
        {#each week as day}
        <div class="trackCard {day.isToday ? 'today' : ''}">
            <h3>{day.name}</h3>
            <p>Books you read:</p>
            {#each matchTrackToDate(day.raw_date) as track}
                <p>{track.title}</p>
            {/each}
            <p>{day.date}</p>
            <button onclick={() => (showModal = !showModal)} style="display: {day.isToday ? 'inline' : 'none'};">Read today</button>
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
            <input type="text"
                onkeyup={
                    async (e) => {
                        current_page = e.currentTarget.value;
                    }
                }>
            <h4>Last page:</h4>
            <input type="text"
                onkeyup={
                    async (e) => {
                        last_page = e.currentTarget.value;
                    }
                }>
            <button onclick={() => markAsRead(info.book_id)}>Mark as read</button>
        </div>
        {/each}
    </div>
{/if}

<style>
    div {
        border: 1px #000 solid;
        display: flex;
        justify-content: space-between;
    }

    .trackCard {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 2%;
    }

    .trackCard.today {
        background-color: #999;
    }

    .books {
        flex-direction: column;
    }
</style>