<script lang="ts">
    import { enhance } from '$app/forms';
    import type { PageData, ActionData } from './$types';
    import { goto } from '$app/navigation';
    let { form }: { form: ActionData } = $props();
</script>

<svelte:head>
  <title>Sign up</title>
</svelte:head>

<h1>Sign up</h1>
<form method="POST" use:enhance={() => {
  return async ({ result, update }) => {
    console.log(result);
    
  if (result.type === 'redirect') {
    goto(result.location);
    return;
  }
  
    update({ reset: false });
  }
}}>
    <label for="username">Username</label>
    <input type="username" name="username" id="username" required />
  
    <label for="email">Email</label>
    <input type="email" name="email" id="email" required />

    <label for="password">Password</label>
    <input type="password" name="password" required />

    <label for="paspassword_againsword">Repeat password</label>
    <input type="password" name="password_again" required />

    <button type="submit">Sign up</button>

  {#if form?.error}
    <div class="error">
        <p>{form.error}</p>
    </div>
  {/if}
</form>

<p>Already have an account?</p>
<a href="/login">Login</a>

<style>
  form {
    display: flex;
    flex-direction: column;
    width: 20vw;
    height: 35vh;
  }

  form input {
    margin-bottom: 3%;
  }

  a {
    font-weight: 600;
  }
</style>