# Create the JavaScript file for interactivity
js_content = '''// Dashboard JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all dashboard functionality
    initializeTabs();
    initializeMetricCounters();
    initializeBrandCards();
    initializeSortableTables();
    initializeKeyboardNavigation();
    initializeModal();
    
    // Tab Navigation System
    function initializeTabs() {
        const tabButtons = document.querySelectorAll('.nav-tab');
        const tabContents = document.querySelectorAll('.tab-content');
        
        tabButtons.forEach((button, index) => {
            button.addEventListener('click', function() {
                const targetTab = this.getAttribute('data-tab');
                activateTab(targetTab, tabButtons, tabContents);
            });
        });
    }
    
    function activateTab(targetTab, tabButtons, tabContents) {
        // Remove active class from all tabs and contents
        tabButtons.forEach(btn => btn.classList.remove('active'));
        tabContents.forEach(content => content.classList.remove('active'));
        
        // Add active class to selected tab and content
        document.querySelector(`[data-tab="${targetTab}"]`).classList.add('active');
        document.getElementById(targetTab).classList.add('active');
        
        // Smooth scroll to content area
        document.querySelector('.dashboard-content').scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
    
    // Keyboard Navigation (1-5 keys for tabs)
    function initializeKeyboardNavigation() {
        document.addEventListener('keydown', function(e) {
            const tabMap = {
                '1': 'portfolio',
                '2': 'brands', 
                '3': 'ppc',
                '4': 'traffic',
                '5': 'objectives'
            };
            
            if (tabMap[e.key]) {
                e.preventDefault();
                const tabButtons = document.querySelectorAll('.nav-tab');
                const tabContents = document.querySelectorAll('.tab-content');
                activateTab(tabMap[e.key], tabButtons, tabContents);
            }
            
            // ESC key to close modal
            if (e.key === 'Escape') {
                closeModal();
            }
        });
    }
    
    // Animated Metric Counters
    function initializeMetricCounters() {
        const metricValues = document.querySelectorAll('.metric-value[data-target]');
        
        metricValues.forEach(element => {
            const target = parseFloat(element.getAttribute('data-target'));
            const prefix = element.textContent.includes('$') ? '$' : '';
            const suffix = '';
            
            animateCounter(element, 0, target, 2000, prefix, suffix);
        });
    }
    
    function animateCounter(element, start, end, duration, prefix = '', suffix = '') {
        const startTime = performance.now();
        
        function updateCounter(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            // Use easing function for smooth animation
            const easedProgress = easeOutQuart(progress);
            const current = start + (end - start) * easedProgress;
            
            // Format number based on magnitude
            let displayValue;
            if (end > 1000) {
                displayValue = Math.floor(current).toLocaleString();
            } else {
                displayValue = current.toFixed(2);
            }
            
            element.textContent = prefix + displayValue + suffix;
            
            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                // Final value formatting
                if (end > 1000) {
                    element.textContent = prefix + Math.floor(end).toLocaleString() + suffix;
                } else {
                    element.textContent = prefix + end.toFixed(2) + suffix;
                }
            }
        }
        
        requestAnimationFrame(updateCounter);
    }
    
    function easeOutQuart(t) {
        return 1 - Math.pow(1 - t, 4);
    }
    
    // Brand Cards Interactivity
    function initializeBrandCards() {
        const brandCards = document.querySelectorAll('.brand-card.clickable');
        
        brandCards.forEach(card => {
            card.addEventListener('click', function() {
                const brandData = getBrandData(this.getAttribute('data-brand'));
                showBrandModal(brandData);
            });
            
            // Add hover effect
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-5px)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
            });
        });
    }
    
    function getBrandData(brandId) {
        const brandData = {
            lunovus: {
                name: 'Lunovus',
                revenue: '$78,359.56',
                momGrowth: '-0.3%',
                yoyGrowth: '+11.3%',
                portfolioShare: '59.5%',
                rating: 'Strong',
                units: '2,846',
                avgPrice: '$27.53',
                sessions: '5,568',
                conversionRate: '51.1%',
                ppc: {
                    spend: '$6,588.37',
                    sales: '$18,555.35',
                    acos: '35.5%',
                    tacos: '8.4%',
                    roas: '2.82',
                    momSalesChange: '+12.1%'
                }
            },
            maxivision: {
                name: 'MaxiVision',
                revenue: '$32,179.47',
                momGrowth: '+3.0%',
                yoyGrowth: '+10.0%',
                portfolioShare: '24.4%',
                rating: 'Good',
                units: '597',
                avgPrice: '$53.90',
                sessions: '3,161',
                conversionRate: '18.9%',
                ppc: {
                    spend: '$1,255.19',
                    sales: '$4,999.13',
                    acos: '25.1%',
                    tacos: '3.9%',
                    roas: '3.98',
                    momSalesChange: '+134.0%'
                }
            },
            advanced: {
                name: 'Advanced Theraceuticals',
                revenue: '$21,162.52',
                momGrowth: '+21.2%',
                yoyGrowth: '+5.7%',
                portfolioShare: '16.1%',
                rating: 'Accelerating',
                units: '608',
                avgPrice: '$34.81',
                sessions: '1,917',
                conversionRate: '31.7%',
                ppc: {
                    spend: '$4,535.59',
                    sales: '$5,364.76',
                    acos: '84.5%',
                    tacos: '21.4%',
                    roas: '1.18',
                    momSalesChange: '+48.9%'
                }
            }
        };
        
        return brandData[brandId];
    }
    
    // Modal Functionality
    function initializeModal() {
        const modal = document.getElementById('brandModal');
        const closeBtn = document.querySelector('.close');
        
        closeBtn.addEventListener('click', closeModal);
        
        window.addEventListener('click', function(event) {
            if (event.target === modal) {
                closeModal();
            }
        });
    }
    
    function showBrandModal(brandData) {
        const modal = document.getElementById('brandModal');
        const modalContent = document.getElementById('modalContent');
        
        const statusClass = brandData.rating.toLowerCase();
        const growthClass = brandData.momGrowth.includes('+') ? 'positive' : 'negative';
        
        modalContent.innerHTML = `
            <h2>${brandData.name} - Detailed Performance</h2>
            <div class="modal-brand-header">
                <span class="brand-status ${statusClass}">${brandData.rating}</span>
            </div>
            
            <div class="modal-metrics-grid">
                <div class="modal-section">
                    <h3>Revenue Performance</h3>
                    <div class="modal-metric-group">
                        <div class="modal-metric">
                            <span class="label">May 2025 Revenue:</span>
                            <span class="value">${brandData.revenue}</span>
                        </div>
                        <div class="modal-metric">
                            <span class="label">Month-over-Month Growth:</span>
                            <span class="value ${growthClass}">${brandData.momGrowth}</span>
                        </div>
                        <div class="modal-metric">
                            <span class="label">Year-over-Year Growth:</span>
                            <span class="value positive">${brandData.yoyGrowth}</span>
                        </div>
                        <div class="modal-metric">
                            <span class="label">Portfolio Share:</span>
                            <span class="value">${brandData.portfolioShare}</span>
                        </div>
                    </div>
                </div>
                
                <div class="modal-section">
                    <h3>Operational Metrics</h3>
                    <div class="modal-metric-group">
                        <div class="modal-metric">
                            <span class="label">Units Sold:</span>
                            <span class="value">${brandData.units}</span>
                        </div>
                        <div class="modal-metric">
                            <span class="label">Average Price:</span>
                            <span class="value">${brandData.avgPrice}</span>
                        </div>
                        <div class="modal-metric">
                            <span class="label">Sessions:</span>
                            <span class="value">${brandData.sessions}</span>
                        </div>
                        <div class="modal-metric">
                            <span class="label">Conversion Rate:</span>
                            <span class="value">${brandData.conversionRate}</span>
                        </div>
                    </div>
                </div>
                
                <div class="modal-section">
                    <h3>PPC Performance</h3>
                    <div class="modal-metric-group">
                        <div class="modal-metric">
                            <span class="label">PPC Spend:</span>
                            <span class="value">${brandData.ppc.spend}</span>
                        </div>
                        <div class="modal-metric">
                            <span class="label">PPC Sales:</span>
                            <span class="value">${brandData.ppc.sales}</span>
                        </div>
                        <div class="modal-metric">
                            <span class="label">ACoS:</span>
                            <span class="value">${brandData.ppc.acos}</span>
                        </div>
                        <div class="modal-metric">
                            <span class="label">TACoS:</span>
                            <span class="value">${brandData.ppc.tacos}</span>
                        </div>
                        <div class="modal-metric">
                            <span class="label">ROAS:</span>
                            <span class="value">${brandData.ppc.roas}</span>
                        </div>
                        <div class="modal-metric">
                            <span class="label">MoM Sales Change:</span>
                            <span class="value positive">${brandData.ppc.momSalesChange}</span>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
        
        // Add modal styles
        const modalStyles = `
            <style>
                .modal-brand-header {
                    margin-bottom: 30px;
                }
                .modal-metrics-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                    gap: 30px;
                }
                .modal-section h3 {
                    color: #1e3a8a;
                    margin-bottom: 20px;
                    font-size: 1.2rem;
                    border-bottom: 2px solid #e5e7eb;
                    padding-bottom: 10px;
                }
                .modal-metric-group {
                    display: grid;
                    gap: 15px;
                }
                .modal-metric {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 10px 0;
                    border-bottom: 1px solid #f1f5f9;
                }
                .modal-metric:last-child {
                    border-bottom: none;
                }
                .modal-metric .label {
                    color: #64748b;
                    font-weight: 500;
                }
                .modal-metric .value {
                    font-weight: 600;
                    color: #1e3a8a;
                }
                .modal-metric .value.positive {
                    color: #059669;
                }
                .modal-metric .value.negative {
                    color: #dc2626;
                }
            </style>
        `;
        
        if (!document.querySelector('#modal-styles')) {
            const styleSheet = document.createElement('style');
            styleSheet.id = 'modal-styles';
            styleSheet.innerHTML = modalStyles;
            document.head.appendChild(styleSheet);
        }
    }
    
    function closeModal() {
        const modal = document.getElementById('brandModal');
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
    
    // Sortable Tables
    function initializeSortableTables() {
        const sortableTables = document.querySelectorAll('.data-table.sortable');
        
        sortableTables.forEach(table => {
            const headers = table.querySelectorAll('th[data-sort]');
            
            headers.forEach(header => {
                header.addEventListener('click', function() {
                    const sortKey = this.getAttribute('data-sort');
                    const tbody = table.querySelector('tbody');
                    const rows = Array.from(tbody.querySelectorAll('tr'));
                    
                    // Determine sort direction
                    const currentDirection = this.getAttribute('data-direction') || 'asc';
                    const newDirection = currentDirection === 'asc' ? 'desc' : 'asc';
                    
                    // Clear previous sort indicators
                    headers.forEach(h => {
                        h.removeAttribute('data-direction');
                        h.style.background = '';
                    });
                    
                    // Set new sort indicator
                    this.setAttribute('data-direction', newDirection);
                    this.style.background = '#e5e7eb';
                    
                    // Sort rows
                    const columnIndex = Array.from(header.parentElement.children).indexOf(header);
                    
                    rows.sort((a, b) => {
                        const aVal = a.children[columnIndex].textContent.trim();
                        const bVal = b.children[columnIndex].textContent.trim();
                        
                        // Handle different data types
                        let aNum = parseFloat(aVal.replace(/[$,%+]/g, ''));
                        let bNum = parseFloat(bVal.replace(/[$,%+]/g, ''));
                        
                        if (!isNaN(aNum) && !isNaN(bNum)) {
                            return newDirection === 'asc' ? aNum - bNum : bNum - aNum;
                        } else {
                            return newDirection === 'asc' ? 
                                aVal.localeCompare(bVal) : 
                                bVal.localeCompare(aVal);
                        }
                    });
                    
                    // Re-append sorted rows
                    rows.forEach(row => tbody.appendChild(row));
                    
                    // Add visual feedback
                    tbody.style.opacity = '0.7';
                    setTimeout(() => {
                        tbody.style.opacity = '1';
                    }, 150);
                });
            });
        });
    }
    
    // Smooth scrolling for internal links
    function initializeSmoothScrolling() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }
    
    // Initialize smooth scrolling
    initializeSmoothScrolling();
    
    // Add print functionality
    function initializePrint() {
        // Add print button if needed
        const printBtn = document.createElement('button');
        printBtn.textContent = 'Print Report';
        printBtn.className = 'print-btn';
        printBtn.style.cssText = `
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #3b82f6;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
            z-index: 1000;
        `;
        
        printBtn.addEventListener('click', () => {
            window.print();
        });
        
        document.body.appendChild(printBtn);
    }
    
    // Initialize print functionality
    initializePrint();
    
    // Add loading states and error handling
    function showLoadingState(element) {
        element.style.opacity = '0.6';
        element.style.pointerEvents = 'none';
    }
    
    function hideLoadingState(element) {
        element.style.opacity = '1';
        element.style.pointerEvents = 'auto';
    }
    
    // Performance monitoring
    function logPerformance() {
        if (typeof performance !== 'undefined' && performance.timing) {
            const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
            console.log(`Dashboard loaded in ${loadTime}ms`);
        }
    }
    
    // Log performance after page load
    window.addEventListener('load', logPerformance);
    
    // Add accessibility improvements
    function initializeAccessibility() {
        // Add ARIA labels
        document.querySelectorAll('.nav-tab').forEach((tab, index) => {
            tab.setAttribute('role', 'tab');
            tab.setAttribute('aria-selected', index === 0 ? 'true' : 'false');
        });
        
        document.querySelectorAll('.tab-content').forEach((content, index) => {
            content.setAttribute('role', 'tabpanel');
            content.setAttribute('aria-hidden', index === 0 ? 'false' : 'true');
        });
        
        // Add keyboard focus indicators
        const style = document.createElement('style');
        style.textContent = `
            .nav-tab:focus,
            .brand-card:focus,
            .data-table th:focus {
                outline: 2px solid #3b82f6;
                outline-offset: 2px;
            }
        `;
        document.head.appendChild(style);
    }
    
    // Initialize accessibility features
    initializeAccessibility();
    
    console.log('🚀 Amazon Dashboard loaded successfully!');
    console.log('💡 Use keyboard shortcuts 1-5 to navigate between tabs');
    console.log('🖱️ Click on brand cards for detailed information');
    console.log('📊 Click table headers to sort data');
});'''

# Save the JavaScript file
with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("✅ Created script.js")
print("\n🎉 Complete interactive dashboard created!")
print("\nFiles created:")
print("- amazon_dashboard.html (Main dashboard file)")
print("- style.css (Styling and responsive design)")
print("- script.js (Interactive functionality)")
print("\n📖 To use the dashboard:")
print("1. Save all three files in the same folder")
print("2. Open amazon_dashboard.html in your web browser")
print("3. Use keyboard shortcuts 1-5 to navigate tabs")
print("4. Click brand cards for detailed information")
print("5. Click table headers to sort data")
print("6. Use the print button for physical reports")