<script lang="ts">
    import type { PageData, ActionData } from './$types';
    let { data, form }: { data: PageData, form: ActionData } = $props();
    console.log(form?.Success)
</script>

<svelte:head>
  <title>Settings</title>
</svelte:head>

<h1>Settings</h1>
{#if data}
{#if form?.error}
    <p class="error">{form.error}</p>
{:else if form?.Success}
    <p class="success">{form.Success}</p>
{/if}
    <form action="?/edit_user" method="post">
        <h2>Username</h2>
        <input type="text" name="username" value={data.username} required>
        <h2>Email</h2>
        <input type="text" name="email" value={data.email} required>
        <h2>Current password</h2>
        <input type="password" name="current_password">
        <h2>New password</h2>
        <input type="password" name="password">
        <h2>Repeat new password</h2>
        <input type="password" name="password_again">
        <button type="submit">Update user</button>
    </form>
{/if}
<style>
    form {
        width: 20vw;
        display: flex;
        flex-direction: column;
    }

    form input {
        margin-bottom: 4%;
    }
</style>