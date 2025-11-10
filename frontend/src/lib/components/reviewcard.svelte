<script lang="ts">
  import { enhance } from '$app/forms';

  export let review_id: number | string | null = null;
  export let username: string;
  export let user_id: number | string | null = null;
  export let rating: number;
  export let review: string;
  export let title: string | null = null;
  export let book_id: number | null = null;
  export let comments: ReviewComment[] | null;
  export let submitResponse: string | any | null;

  let commentArrow: string = "v";

  console.log(submitResponse)

  function commentFoldToggle() {
    if (commentArrow == ">") {
      commentArrow = "v";
    } else if (commentArrow == "v") {
      commentArrow = ">";
    }
  }
</script>

<div class="review-card">
    <h2 class="book-title">
      <a href={"/book/" + book_id}>{title}</a>
    </h2>
    
    <div class="review-header">
      <a href="/user/{user_id}">
        <h3 class="username">{username}</h3>
      </a>
      <h3 class="spacer">·</h3>
      <div class="stars">
        {#each Array(rating) as _}
          <span>★</span>
        {/each}
      </div>  
  </div>

  <p class="review-text">{review}</p>
  <div id="commentsWrapper">
    <div id="commentsHeader">
      <button onclick={() => commentFoldToggle()}>{commentArrow}</button>
      <h3>Comments ({comments?.length})</h3>
    </div>
    <div id="commentContent" style="display: {commentArrow == "v" ? "flex" : "none"}">
      {#each [...(comments ?? [])].reverse() as comment }
        <div class="comment">
          <h3>{comment.username}</h3>
          <p>{comment.comment_text}</p>
        </div>
      {/each}
    </div>

    <form action="?/create_comment" id="commentForm" method="post" use:enhance={() => {
      return async ({ update }) => {
        update({ reset: false });
      };
    }}>
      <input type="text" name="review_id" value={review_id} hidden>
      <textarea name="comment_text"></textarea>
      <button>Add a comment</button>

      {#if submitResponse}
        <div class="notice error">
          {submitResponse.error}
        </div>
      {/if}
    </form>
  </div>
</div>

<style>
  .review-card {
    background: #e9edc9;
    border-radius: 5px;
    padding: 1rem;
    margin-bottom: 1rem;
  }
  .review-header {
    display: flex;
    align-items: center;
  }
  .review-header .spacer {
    width: 1vw;
    text-align: center;
  }

  .stars {
    width: 4vw;
    color: gold;
    font-size: 2em;
  }

  .review-text {
    padding-bottom: 1vw;
  }

  #commentsWrapper {
    width: 25vw;
  }
  #commentsHeader {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-bottom: 1%;
  }
  
  #commentContent {
    max-height: 40vh;
    flex-direction: column;
    overflow-y: scroll;
    margin-bottom: 1%;
  }

  .comment {
    background-color: #fefae0;
    padding: 2%;
    margin-bottom: 1%;
    border-radius: 5px;
  }

  #commentForm {
    display: flex;
    flex-direction: column;
  }

  #commentForm textarea {
    height: 10vh;
    margin-bottom: 2%;
  }
</style>