<script lang="ts">
    import type { PageData } from './$types';
    import Reviewcard from '$lib/components/reviewcard.svelte';
    let { data }: { data: PageData } = $props();

    const listnames = ["Want to read", "Reading", "Finished", "Didn't finish"];
</script>

<svelte:head>
  <title>{data.username}</title>
</svelte:head>
<h1>{data.username}</h1>

<id id="listWrapper">
    {#each listnames as list}
    <div class="list">
        <h2>{list}</h2>
        {#each data.books as b}
        {#if b.book_status == list}
        <a href="/book/{b.book_id}"><p>{b.title}</p></a>
        {/if}
        {/each}
    </div>
    {/each}
</id>

<h2>Reviews by {data.username}</h2>
{#if data.reviews.length > 0}
    {#each data.reviews as review}
        <Reviewcard
            book_id={review.book_id}
            title={review.title}
            username={review.username}
            user_id={data.user_id!}
            rating={review.rating}
            review={review.review}
        />
    {/each}
{/if}

<style>
    #listWrapper {
        display: grid;
        grid-template-columns: 25% 25% 25% 25%;
        padding: 1rem 20%;
        background-color: #e9edc9;
        border-radius: 5px;
        margin-bottom: 1%;
        min-height: 37vh;
    }

    .list {
        border-right: 2px solid #ccd5ae;
        padding-left: 4%;
    }

    .list:first-child {
        padding: none;
    }

    .list:last-child {
        border: none;
    }
</style>