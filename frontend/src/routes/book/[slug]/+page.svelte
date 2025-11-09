    <script lang="ts">
        import type { PageData, ActionData } from './$types';
        import Reviewcard from '$lib/components/reviewcard.svelte';
        let { data, form }: { data: PageData, form: ActionData } = $props();
        let listval = $state();
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

    <svelte:head>
        <title>{data.title}</title>
    </svelte:head>

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
                    <h3>{Math.round(data.average_rating * 10) / 10}</h3>
                </div>
                <p>{data.summary}</p>
                <div id="addToListWrapper">
                    <form method="POST" action={method}>
                        {#if form?.duplicate_error}<p class="error">You've already added this book to a list.</p>{/if}
                        <input type="hidden" name="book_id" value={data.book_id}>
                        
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
            <div></div>
            <div id="reviewsSection">
                <h3>Write a review</h3>
                {#if form?.duplicate_error}<p class="error">You've already reviewed this book</p>{/if}
                <form method="POST" id="createReview" action="?/create_review">
                    <input type="hidden" name="book_id" value={data.book_id}>
                    <h4>Rating</h4><input name="rating" type="number">
                    <textarea name="reviewtext" id="" rows="10"></textarea>
                    <button>Submit</button>
                </form>
                
                {#if data.reviews.length > 0}
                {#each data.reviews as review}
                <Reviewcard
                    username={review.username}
                    rating={review.rating}
                    review={review.review}
                    />
                {/each}
                
                {:else}
                    <h2>No reviews yet.</h2>
                {/if}
            </div>
        </div>
    {/if}

    <style>
        #bookCover {
            justify-content: center;
            display: flex;
            grid-area: cover;
        }

        #bookCover img {
            max-width: 100%;
            max-height: 80vh;
        }
        #bookWrapper {
            display: grid;
            grid-template-columns: 35% 32%;
            grid-template-areas:
                    "cover info" 
                    "cover review";
        }

        #bookDetails {
            grid-area: info;
        }

        #subHeader {
            display: flex;
            width: 15vw;
            flex-direction: row;
            justify-content: space-between;
        }
        #lists {
            background-color: #fff;
            width: 15vw;
            box-sizing: border-box;
            border-radius: 5px;
            padding: 7px 10px;
            font-size: 1em;
            border: none;
        }

        #reviewsSection {
            grid-area: review;
        }

        #createReview {
            display: flex;
            flex-direction: column;
        }

        #createReview button, #createReview input, #createReview textarea {
            margin-bottom: 2%;
        }

        #createReview input::-webkit-outer-spin-button,
        #createReview input::-webkit-inner-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }
        #createReview input {
            -moz-appearance: textfield;
            appearance: textfield;
        }
    </style>