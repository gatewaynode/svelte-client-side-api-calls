<script lang="ts">
    import { post_stuff } from "$lib/components/call_fapi";
    import { fetch_table } from "$lib/components/call_fapi";
    import { Tabulator } from "tabulator-tables";
    import { onMount } from "svelte";

    let post_body = JSON.stringify({
        name: "fish",
        description: "This is a test product",
        plu: 1234567890,
    });

    onMount(() => {
        let path, body, target;
        let tabledata = fetch_table(post_body).then((data) => {
            console.log(data);
            var table = new Tabulator("#demo-table", {
                data: data.rows,
                layout: "fitColumns",
                columns: data.columns,
            });
        });
    });
</script>

<h2>API Call Complex Data plus Tabulator</h2>
<h3 class="label">POST</h3>
<div id="demo-table"></div>

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
