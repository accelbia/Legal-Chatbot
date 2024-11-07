document.querySelectorAll('.menu .button').forEach(button => {
    button.addEventListener('click', function() {
        // Remove the 'clicked' class from all buttons to reset background color
        document.querySelectorAll('.menu .button').forEach(btn => btn.classList.remove('clicked'));
        
        // Add 'clicked' class to the clicked button
        this.classList.add('clicked');
        
        // Determine the URL to fetch content from based on button ID
        let pageUrl;
        switch (this.id) {
            case 'contract-review':
                pageUrl = 'contract_review.html';
                break;
            case 'compliance-check':
                pageUrl = 'compliance-check.html';
                break;
            case 'risk-management':
                pageUrl = 'risk-management.html';
                break;
            case 'document-generation':
                pageUrl = 'document-generation.html';
                break;
            case 'saved-documents':
                pageUrl = 'saved-documents.html';
                break;
            case 'saved-chats':
                pageUrl = 'saved-chats.html';
                break;
            default:
                pageUrl = "main.html";
        }
        
        // Load the specified page content into the main-content div
        fetch(pageUrl)
            .then(response => response.text())
            .then(data => {
                document.querySelector('.main-content').innerHTML = data;
            })
            .catch(error => {
                console.error('Error loading page:', error);
                document.querySelector('.main-content').innerHTML = '<p>Error loading content. Please try again later.</p>';
            });
    });
  });
  