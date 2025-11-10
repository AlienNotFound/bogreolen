<script lang="ts">
    import Reviewcard from "./reviewcard.svelte";

    let { reviews } = $props();

</script>

<div id="reviewCardHolder">
    <h2>Recent reviews of books you're interested in</h2>
    {#each reviews as review}
        <Reviewcard 
                review_id={review.review_id}
                username={review.username}
                user_id={review.user_id}
                rating={review.rating}
                review={review.review}
                title={review.title}
                book_id={review.book_id}
                comments={review.comments}
                />
    {/each}
</div>