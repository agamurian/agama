<script lang="ts">
	import '$lib/styles/main.scss';
	import '$lib/styles/fonts.scss';
	import { bgColor } from '$lib/stores';
</script>

<div
	style="background-color: {$bgColor}; height: 100vh; width:100vw; position: fixed; z-index: -1"
/>
<slot />
