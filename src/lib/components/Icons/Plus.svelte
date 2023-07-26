<script lang="ts">
	import { DEFAULT_ICON_SIZE } from './constants';
	export let size = DEFAULT_ICON_SIZE;
	export let color = 'currentColor';
</script>

<svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} fill={color} viewBox="0 0 11 12">
	<path
		d="M10 6.75H6.25V10.5C6.25 10.9125 5.9125 11.25 5.5 11.25C5.0875 11.25 4.75 10.9125 4.75 10.5V6.75H1C0.5875 6.75 0.25 6.4125 0.25 6C0.25 5.5875 0.5875 5.25 1 5.25H4.75V1.5C4.75 1.0875 5.0875 0.75 5.5 0.75C5.9125 0.75 6.25 1.0875 6.25 1.5V5.25H10C10.4125 5.25 10.75 5.5875 10.75 6C10.75 6.4125 10.4125 6.75 10 6.75Z"
	/>
</svg>
