<script lang="ts">
  import type { ActionData } from './$types';
  import { enhance } from '$app/forms';
  export let form: ActionData;
</script>

<svelte:head>
  <title>Login</title>
</svelte:head>

<h1>Login</h1>
<form method="post" use:enhance>
  <label for="username">Email</label>
  <input type="username" name="username" id="email" required />

  <label for="password">Password</label>
  <input type="password" name="password" id="password" required />

  <button type="submit">Login</button>

  {#if form?.Error}
    <div class="notice error">
      {form.Error}
    </div>
  {/if}
</form>

<div class="actions">
  <p>Don't have an account?</p>
  <a href="/signup">Sign Up</a>
</div>

<style>
  form {
    display: flex;
    flex-direction: column;
    width: 20vw;
    height: 20vh;
  }

  form input {
    margin-bottom: 3%;
  }

  a {
    font-weight: 600;
  }
</style>