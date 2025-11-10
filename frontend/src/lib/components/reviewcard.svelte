<script lang="ts">
  import { enhance } from '$app/forms';

  export let review_id: number | string | null = null;
  export let username: string;
  export let user_id: number | string | null = null;
  export let current_user_id: number | string | null = null;
  export let rating: number;
  export let review: string;
  export let title: string | null = null;
  export let book_id: number | null = null;
  export let comments: ReviewComment[] | null;
  export let submitResponse: string | any | null;

  let method: string = "";
  let editting: boolean = false;
  let commentArrow: string = "v";

  function commentFoldToggle() {
    if (commentArrow == ">") {
      commentArrow = "v";
    } else if (commentArrow == "v") {
      commentArrow = ">";
    }
  }
  
  function switchMethod(val: string) {
    if (val == "edit") {
      if (editting) {
        method = "?/edit_comment";
      }
    } else if (val == "delete") {
      method = "?/delete_comment";
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
          <form action={method} id="commentEditDeleteForm" method="post" use:enhance={({ cancel, submitter }) => { 
            if (submitter?.dataset.action === "delete") {
              if (!window.confirm("Are you sure you want to delete this comment? This cannot be undone!")) {
                cancel();
                return;
              }
            } else if (submitter?.dataset.action === "save") {
              editting = false;
              return;
            }
            
            return async ({ update }) => {
              update({ reset: false });
            };
          }}>
          
          <div class="commentHeader">
            <h3>{comment.username}</h3>
            <div>
          
              {#if current_user_id == comment.user_id}
              <input type="hidden" name="comment_id" value={comment.comment_id}>
              {#if editting}
              <button data-action="save" onclick={() => switchMethod("edit")}>💾</button>
              {:else}
              <button data-action="edit" onclick={() => editting = true}>✏️</button>
              {/if}
              <button data-action="delete" onclick={() => switchMethod("delete")}>🗑️</button>
              {/if}
          
            </div>
          </div>

            {#if editting && current_user_id == comment.user_id}
            <textarea name="comment_text_edit" value={comment.comment_text}></textarea>
            {:else}
            <p>{comment.comment_text}</p>
            {/if}
          
          </form>
        </div>
      {/each}
    </div>

    <form action="?/create_comment" id="commentForm" method="post" use:enhance={() => {
      return async ({ update }) => {
        update({ reset: false });
      };
    }}>
      <input type="hidden" name="review_id" value={review_id}>
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

  .commentHeader {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: baseline;
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