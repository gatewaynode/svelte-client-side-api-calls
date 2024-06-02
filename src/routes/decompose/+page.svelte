<script>
    import { get_stuff } from "$lib/components/call_fapi";
    import { post_stuff } from "$lib/components/call_fapi";

    let post_body = JSON.stringify({
        name: "fish",
        description: "This is a test product",
        plu: 1234567890,
    });
</script>

<h1>API Call Component Testing</h1>
<div class="something">
    {#await get_stuff()}
        ...await...
    {:then payload}
        <h3 class="label">GET</h3>
        {payload.message}
    {/await}
</div>
<div class="something">
    {#await post_stuff(post_body)}
        ...await...
    {:then payload}
        <h3 class="label">POST</h3>
        <div>{payload.name}</div>
        <div>{payload.description}</div>
        <div>{payload.plu}</div>
    {/await}
</div>

<style>
    .something {
        border: 1px solid rgb(134, 54, 54);
        padding: 1em;
        margin: 1em;
    }
    .label {
        color: rgb(117, 108, 198);
    }
</style>
