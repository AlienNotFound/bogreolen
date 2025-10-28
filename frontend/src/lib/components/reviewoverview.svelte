<script lang="ts">
    import { onMount } from "svelte";

    type Review = {
        bookid: number,
        title: string,
        rating: number,
        username: string,
        review: string
    }

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
    <div class="reviewCard">
        <h3>{review.username} wrote a review on {review.title}</h3>
        <h4>{review.rating}</h4>
        <p>{review.review}</p>
    </div>
    {/each}
</div>

<style>
    .reviewCard     {
        border: 1px solid #000;
        padding: 1% 2%;
        margin-bottom: 1%;
        width: 20vw;
    }
</style>