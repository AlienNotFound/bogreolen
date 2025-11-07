<script lang="ts">
  export let username: string;
  export let user_id: number;
  export let rating: number;
  export let review: string;
  export let title: string | null = null;
  export let book_id: number | null = null;
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
  <button>Add a comment</button>
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
</style>