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
        <h2>GET</h2>
        {payload.message}
    {/await}
</div>
<div class="something">
    {#await post_stuff(post_body)}
        ...await...
    {:then payload}
        <h2>POST</h2>
        {payload.name}
        {payload.description}
        {payload.plu}
    {/await}
</div>

<style>
    .something {
        border: 1px solid rgb(134, 54, 54);
        padding: 1em;
        margin: 1em;
    }
</style>
