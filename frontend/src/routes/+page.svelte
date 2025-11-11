<script lang="ts">
    import Trackingoverview from '$lib/components/trackingoverview.svelte';
    import Reviewcard from '$lib/components/reviewcard.svelte';
    import type { PageData, ActionData } from './$types.js';
    let { data, form }: { data: PageData, form: ActionData } = $props();
</script>

<svelte:head>
  <title>The Bookshelf</title>
</svelte:head>

<Trackingoverview tracks={data.tracks ?? []}
                    modalInfo={data.modalInfo ?? []} 
                    />

<div id="reviewCardHolder">
    <h2>Recent reviews of books you're interested in</h2>
    {#each data.reviews as review}
        <Reviewcard 
                review_id={review.review_id}
                username={review.username}
                user_id={review.user_id}
                current_user_id={data.user_id}
                rating={review.rating}
                review={review.review}
                title={review.title}
                book_id={review.book_id}
                comments={review.comments}
                submitResponse={form}
                />
    {/each}
</div>