<script>
    import Searchbar from '$lib/components/searchbar.svelte';
    import Trackingoverview from '$lib/components/trackingoverview.svelte';
    import Reviewoverview from '$lib/components/reviewoverview.svelte';
    export let data;
</script>

<Searchbar />
<Trackingoverview tracks={data.tracks ?? []}
                    modalInfo={data.modalInfo ?? []} 
                    />
<Reviewoverview reviews={data.reviews}/>