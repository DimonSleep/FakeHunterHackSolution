    // Function to handle the button click and find the source
    sourceButton.addEventListener("click", function () {
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            const currentTab = tabs[0];
            
            // Extract simplified query from the title
            let simplifiedQuery = currentTab.title.split(' ').slice(0, 5).join(' '); // Taking only the first 5 words for better match

            // Function to call NewsAPI for different languages
            const fetchSourceFromNewsAPI = (language) => {
                const apiUrl = `https://newsapi.org/v2/everything?apiKey=${apiKey}&q=${encodeURIComponent(simplifiedQuery)}&language=${language}`;
                
                return fetch(apiUrl)
                    .then(response => response.json())
                    .then(data => {
                        if (data.articles && data.articles.length > 0) {
                            const article = data.articles[0]; // Get the most relevant article
                            return {
                                source: article.source.name || 'Sursă necunoscută',
                                title: article.title || 'Titlu indisponibil',
                                url: article.url || 'URL indisponibil'
                            };
                        } else {
                            return null; // No article found
                        }
                    })
                    .catch(error => {
                        console.error('Error fetching source from :', error);
                        return null;
                    });
            };

            // Run NewsAPI search for multiple languages (Romanian, English, Russian)
            Promise.all([
                fetchSourceFromNewsAPI('ro'),
                fetchSourceFromNewsAPI('en'),
                fetchSourceFromNewsAPI('ru'),
                fetchSourceFromNewsAPI('md')
            ]).then(results => {
                const foundSource = results.find(result => result !== null);

                if (foundSource) {
                    // Display the found source information
                    sourceInfo.innerHTML = `
                        <p><strong>Sursa Originală:</strong> ${foundSource.source}</p>
                        <p><strong>Titlu:</strong> ${foundSource.title}</p>
                        <p><strong>Link către articol:</strong> <a href="${foundSource.url}" target="_blank">${foundSource.url}</a></p>
                    `;
                } else {
                    // No source found for any language
                    sourceInfo.innerHTML = '<p>Nu s-a găsit nicio sursă relevantă pentru acest articol prin in baza noastra.</p>';
                }
            });
        });
    });
