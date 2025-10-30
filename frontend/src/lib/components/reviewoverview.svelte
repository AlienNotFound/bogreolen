<script lang="ts">
    import { onMount } from "svelte";
    import Reviewcard from "./reviewcard.svelte";

    let reviews = $state<Review[]>([]);
    let loading = $state(true);

    async function fetchReviews() {
        try {
            const response = await fetch('http://localhost:8000/reviews/book/1')
            reviews = await response.json();
            console.log("reviews", reviews);
        } catch (err) {
            console.error(err);
        } finally {
            loading = false;
        }
    }

    onMount(() => {
        fetchReviews();
    })

</script>

<div id="reviewCardHolder">
    <h2>Nyeste anmeldelser på bøger du er interesserede i</h2>
    {#each reviews as review}
        <Reviewcard 
                username={review.username}
                rating={review.rating}
                review={review.review}
                title={review.title}
                book_id={review.book_id}
                />
    {/each}
</div>