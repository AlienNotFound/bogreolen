<script lang="ts">
    import Reviewcard from "./reviewcard.svelte";

    let { reviews } = $props();

</script>

<div id="reviewCardHolder">
    <h2>Recent reviews of books you're interested in</h2>
    {#each reviews as review}
        <Reviewcard 
                username={review.username}
                user_id={review.userid}
                rating={review.rating}
                review={review.review}
                title={review.title}
                book_id={review.book_id}
                />
    {/each}
</div>