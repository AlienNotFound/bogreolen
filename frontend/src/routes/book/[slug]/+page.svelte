<script lang="ts">
    import { enhance } from '$app/forms';
    import type { PageData, ActionData } from './$types';
    let { data, form }: { data: PageData, form: ActionData } = $props();
    let listval = $state();
    console.log(data.book_status);
    const method = data.book_status ? "?/move_to_list" : "?/add_to_list";

    const listMap: Record<string, string> = {
        "Want to read": "WANT_TO_READ",
        "Reading": "READING",
        "Finished": "FINISHED",
        "Didn't finish": "DIDNTFINISH"
    };

    if (data.book_status) {
        listval = listMap[data.book_status] ?? '';
    }

</script>

{#if data && data.title}
<div id="bookWrapper">
    <div id="bookCover">
        <img src={data.image} alt="Bog cover" />
        </div>
        <div id="bookDetails">
            <h1>{data.title}</h1>
            <div id="subHeader">
                <h3>{data.author_name}</h3>
                <h3>·</h3>
                <h3>{data.category_title}</h3>
                <h3>·</h3>
                <h3>{data.year}</h3>
                <h3>·</h3>
                <h3>{data.average_rating}</h3>
            </div>
            <p>{data.summary}</p>
            <div id="addToListWrapper">
                <form method="POST" action={method} use:enhance>
                    {#if form?.duplicate_error}<p class="error">You've already added this book to a list.</p>{/if}
                    <input type="hidden" name="bookid" value={data.bookid}>
    
                    <select name="listname" id="lists" bind:value={listval}>
                        <option value="WANT_TO_READ">Want to read</option>
                        <option value="READING">Reading</option>
                        <option value="FINISHED">Finished</option>
                        <option value="DIDNTFINISH">Didn't finish</option>
                    </select>
    
                    <button type="submit" disabled={!listval}>Submit</button>
                </form>
            </div>
        </div>
        <div id="reviewsSection">
            {#if data.reviews.length > 0}
                {#each data.reviews as review}
                    <h2>Skrevet af {review.username}</h2>
                    <div id="reviewStars">
                        {#each { length: review.rating} }
                            <h2>★</h2>
                        {/each}
                    </div>
                    <div id="reaviewText">
                        <p>{review.review}</p>
                    </div>
                {/each}
            
            {:else}
                <h2>No reviews yet.</h2>
            {/if}
        </div>
    </div>
{/if}

<style>
    #bookWrapper {
        display: grid;
        grid-template-columns: 35% 45%;
    }

    #subHeader {
        width: 15vw;
        flex-direction: row;
        justify-content: space-between;
    }

    #reviewStars {
        width: 15vw;
    }
    
    #reviewStars, #subHeader {
        display: flex;
    }
</style>