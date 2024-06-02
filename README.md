# Why Client Side Calls are abit tricky in a SvelteKit SPA

The SvelteKit loading functions are great, but seem to expect to be launching from a JS runtime stack.  Most of the examples and demos I found online where pretty sparse if not outright wrong, this is more or less working for me against a FastAPI implementation I stood up on another box (the 192.168.1.99 LAN address).

I'll see if I can get +page.js/+page.ts working and document here 

If you have python and poetry installed the server can be setup with:

```bash
cd api-server
poetry install
poetry shell
fastapi run
```

# create-svelte

Everything you need to build a Svelte project, powered by [`create-svelte`](https://github.com/sveltejs/kit/tree/main/packages/create-svelte).

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```bash
# create a new project in the current directory
npm create svelte@latest

# create a new project in my-app
npm create svelte@latest my-app
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```bash
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```bash
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://kit.svelte.dev/docs/adapters) for your target environment.
