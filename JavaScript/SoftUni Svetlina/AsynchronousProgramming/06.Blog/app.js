function attachEvents() {
    console.log('TODO...');

    const btnLoadPosts = document.getElementById('btnLoadPosts');
    const btnViewPost = document.getElementById('btnViewPost');
    
    const posts = document.getElementById('posts');
    
    const postTitle = document.getElementById('post-title');
    const postBody = document.getElementById('post-body');
    const postComments = document.getElementById('post-comments');

    btnLoadPosts.addEventListener('click', loadPosts);
    btnViewPost.addEventListener('click', viewPost);

    async function loadPosts() {
        const serverPosts = await (await fetch('http://localhost:3030/jsonstore/blog/posts')).json();

        for (const postId in serverPosts) {
            const post = serverPosts[postId];

            const option = document.createElement('option');
            option.value = post.id;
            option.innerHTML = post.title;

            posts.appendChild(option);
        }
    }

    async function viewPost() {
        const currentPostId = posts.value;

        const curerntPost =  await (await fetch(`http://localhost:3030/jsonstore/blog/posts/${currentPostId}`)).json();
        const comments = await (await fetch(`http://localhost:3030/jsonstore/blog/comments/`)).json();
        
        postTitle.innerHTML = curerntPost.title;
        postBody.innerHTML = curerntPost.body;
        
        for (const commentId in comments) {
            const comment = comments[commentId];
            const li = document.createElement('li');
            
            if (comment.postId == currentPostId) {
                li.innerHTML = comment.text;
                postComments.appendChild(li);
            }
            


        }
    }
}

attachEvents();