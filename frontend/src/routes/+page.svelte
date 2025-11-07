<script>
    import Searchbar from '$lib/components/searchbar.svelte';
    import Trackingoverview from '$lib/components/trackingoverview.svelte';
    import Reviewoverview from '$lib/components/reviewoverview.svelte';
    export let data;
</script>

<svelte:head>
  <title>The Bookshelf</title>
</svelte:head>

<Trackingoverview tracks={data.tracks ?? []}
                    modalInfo={data.modalInfo ?? []} 
                    />
<Reviewoverview reviews={data.reviews}/>