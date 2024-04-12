<script>
  // Importing Svelte modules
  import { onMount } from 'svelte';

  // Note object structure
  let note = {
    title: '',
    content: ''
  };

  // Function to create a new note
  async function createNote() {
    try {
      const response = await fetch('http://localhost:8000/notes/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(note)
      });

      if (response.ok) {
        console.log('Note created successfully');
        // Reset the note object after successful creation
        note = { title: '', content: '' };
      } else {
        console.error('Failed to create note');
      }
    } catch (error) {
      console.error('Error creating note:', error);
    }
  }

  // Function to handle form submission
  function handleSubmit(event) {
    event.preventDefault();
    createNote();
  }
</script>

<!-- HTML template for the component -->
<div>
  <h2>Create a New Note</h2>
  <form on:submit={handleSubmit}>
    <div>
      <label for="title">Title:</label>
      <input type="text" id="title" bind:value={note.title} required />
    </div>
    <div>
      <label for="content">Content:</label>
      <textarea id="content" bind:value={note.content} required />
    </div>
    <button type="submit">Create Note</button>
  </form>
</div>

