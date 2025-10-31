<script lang="ts">
  import type { ActionData } from './$types';
  import { enhance } from '$app/forms';
  export let form: ActionData;
</script>

<svelte:head>
  <title>Login</title>
</svelte:head>

<h1>Login</h1>

<section>
  <form method="post" use:enhance>
    <div class="group">
      <label for="username">Email</label>
      <input type="username" name="username" id="email" required />
    </div>

    <div class="group">
      <label for="password">Password</label>
      <input type="password" name="password" id="password" required />
    </div>

    <div class="submit-container">
      <button type="submit">Login</button>
    </div>

    {#if form?.Error}
      <div class="notice error">
        {form.Error}
      </div>
    {/if}
  </form>

  <div class="actions">
    <a href="/signup">Sign Up</a>
  </div>
</section>