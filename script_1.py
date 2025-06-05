# Create the CSS file for styling
css_content = '''/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f8fafc;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Header Styles */
.dashboard-header {
    background: linear-gradient(135deg, #1e3a8a, #3b82f6);
    color: white;
    padding: 40px 0;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.dashboard-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 10px;
    letter-spacing: 1px;
    text-align: center;
}

.dashboard-subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
    margin-bottom: 30px;
    text-align: center;
}

.executive-summary {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 30px;
    margin-top: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.executive-summary h2 {
    font-size: 1.5rem;
    margin-bottom: 15px;
    color: #fbbf24;
}

.executive-summary p {
    font-size: 1.1rem;
    line-height: 1.8;
}

/* Metrics Overview */
.metrics-overview {
    padding: 40px 0;
    background: white;
    border-bottom: 1px solid #e5e7eb;
}

.metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}

.metric-card {
    background: white;
    border-radius: 12px;
    padding: 30px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    border: 1px solid #e5e7eb;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
}

.metric-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(135deg, #3b82f6, #1e3a8a);
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 10px;
}

.metric-label {
    font-size: 1rem;
    color: #64748b;
    margin-bottom: 10px;
    font-weight: 500;
}

.metric-change {
    font-size: 0.9rem;
    font-weight: 600;
    padding: 5px 15px;
    border-radius: 20px;
    display: inline-block;
}

.metric-change.positive {
    background: #dcfce7;
    color: #166534;
}

.metric-change.negative {
    background: #fee2e2;
    color: #dc2626;
}

.metric-change.warning {
    background: #fef3c7;
    color: #d97706;
}

/* Tab Navigation */
.tab-navigation {
    background: white;
    border-bottom: 1px solid #e5e7eb;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.nav-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 0;
}

.nav-tab {
    background: none;
    border: none;
    padding: 20px 30px;
    font-size: 1rem;
    font-weight: 600;
    color: #64748b;
    cursor: pointer;
    transition: all 0.3s ease;
    border-bottom: 3px solid transparent;
    position: relative;
    white-space: nowrap;
}

.nav-tab:hover {
    color: #3b82f6;
    background: #f8fafc;
}

.nav-tab.active {
    color: #1e3a8a;
    border-bottom-color: #3b82f6;
    background: #f8fafc;
}

/* Dashboard Content */
.dashboard-content {
    background: #f8fafc;
    min-height: 600px;
    padding: 40px 0;
}

.tab-content {
    display: none;
    animation: fadeIn 0.3s ease-in-out;
}

.tab-content.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.tab-content h2 {
    font-size: 2rem;
    color: #1e3a8a;
    margin-bottom: 30px;
    font-weight: 700;
}

.tab-content h3 {
    font-size: 1.5rem;
    color: #374151;
    margin-bottom: 20px;
    font-weight: 600;
}

/* Overview Grid */
.overview-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 30px;
    margin-bottom: 30px;
}

.overview-section {
    background: white;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    border: 1px solid #e5e7eb;
}

/* Data Tables */
.data-table {
    width: 100%;
    border-collapse: collapse;
    background: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.data-table th {
    background: #f8fafc;
    padding: 15px;
    text-align: left;
    font-weight: 600;
    color: #374151;
    border-bottom: 2px solid #e5e7eb;
    position: relative;
}

.data-table.sortable th {
    cursor: pointer;
    user-select: none;
}

.data-table.sortable th:hover {
    background: #f1f5f9;
}

.data-table.sortable th::after {
    content: '↕';
    position: absolute;
    right: 10px;
    color: #9ca3af;
    font-size: 0.8rem;
}

.data-table td {
    padding: 15px;
    border-bottom: 1px solid #f1f5f9;
}

.data-table tr:hover {
    background: #f8fafc;
}

.data-table .positive {
    color: #059669;
    font-weight: 600;
}

.data-table .negative {
    color: #dc2626;
    font-weight: 600;
}

.data-table .warning {
    color: #d97706;
    font-weight: 600;
}

/* Brand Cards */
.brand-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-bottom: 40px;
}

.brand-card {
    background: white;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    border: 1px solid #e5e7eb;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
}

.brand-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.brand-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.brand-header h3 {
    font-size: 1.3rem;
    color: #1e3a8a;
    margin: 0;
}

.brand-status {
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.9rem;
    font-weight: 600;
}

.brand-status.strong {
    background: #dcfce7;
    color: #166534;
}

.brand-status.good {
    background: #dbeafe;
    color: #1e40af;
}

.brand-status.accelerating {
    background: #fef3c7;
    color: #d97706;
}

.brand-metrics {
    display: grid;
    gap: 15px;
}

.brand-metric {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid #f1f5f9;
}

.brand-metric:last-child {
    border-bottom: none;
}

.brand-metric .metric-label {
    color: #64748b;
    font-weight: 500;
}

.brand-metric .metric-value {
    font-weight: 600;
    color: #1e3a8a;
}

.brand-metric .metric-value.positive {
    color: #059669;
}

.brand-metric .metric-value.negative {
    color: #dc2626;
}

/* Brand Summary Table */
.brand-summary-table {
    background: white;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    border: 1px solid #e5e7eb;
}

.status {
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
}

.status.strong {
    background: #dcfce7;
    color: #166534;
}

.status.good {
    background: #dbeafe;
    color: #1e40af;
}

.status.accelerating {
    background: #fef3c7;
    color: #d97706;
}

/* PPC Performance */
.ppc-overview {
    background: white;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    border: 1px solid #e5e7eb;
    margin-bottom: 30px;
}

.ppc-metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.ppc-metric {
    text-align: center;
    padding: 20px;
    border-radius: 8px;
    background: #f8fafc;
    border: 1px solid #e5e7eb;
}

.ppc-metric .metric-label {
    display: block;
    color: #64748b;
    font-size: 0.9rem;
    margin-bottom: 10px;
}

.ppc-metric .metric-value {
    display: block;
    font-size: 1.8rem;
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 5px;
}

.ppc-metric .metric-change {
    font-size: 0.8rem;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 12px;
}

/* Traffic Analysis */
.traffic-overview {
    background: white;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    border: 1px solid #e5e7eb;
    margin-bottom: 30px;
}

.traffic-metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.traffic-metric {
    text-align: center;
    padding: 20px;
    border-radius: 8px;
    background: #f8fafc;
    border: 1px solid #e5e7eb;
}

.traffic-metric .metric-label {
    display: block;
    color: #64748b;
    font-size: 0.9rem;
    margin-bottom: 10px;
}

.traffic-metric .metric-value {
    display: block;
    font-size: 1.8rem;
    font-weight: 700;
    color: #1e3a8a;
    margin-bottom: 5px;
}

.traffic-metric .metric-change {
    font-size: 0.8rem;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 12px;
}

/* Strategic Objectives */
.objectives-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 20px;
}

.objective-card {
    background: white;
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    border: 1px solid #e5e7eb;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.objective-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 25px rgba(0, 0, 0, 0.1);
}

.objective-card h3 {
    color: #1e3a8a;
    margin-bottom: 15px;
    font-size: 1.2rem;
}

.objective-card p {
    color: #4b5563;
    line-height: 1.6;
}

/* Modal Styles */
.modal {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(5px);
}

.modal-content {
    background-color: white;
    margin: 5% auto;
    padding: 40px;
    border-radius: 12px;
    width: 90%;
    max-width: 800px;
    max-height: 80vh;
    overflow-y: auto;
    position: relative;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2);
}

.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    position: absolute;
    right: 20px;
    top: 20px;
    cursor: pointer;
}

.close:hover,
.close:focus {
    color: #000;
}

/* Responsive Design */
@media (max-width: 768px) {
    .container {
        padding: 0 15px;
    }
    
    .dashboard-title {
        font-size: 2rem;
    }
    
    .nav-tabs {
        overflow-x: auto;
        white-space: nowrap;
    }
    
    .nav-tab {
        padding: 15px 20px;
        font-size: 0.9rem;
    }
    
    .metrics-grid {
        grid-template-columns: 1fr;
    }
    
    .brand-cards {
        grid-template-columns: 1fr;
    }
    
    .objectives-grid {
        grid-template-columns: 1fr;
    }
    
    .ppc-metrics-grid,
    .traffic-metrics-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .modal-content {
        margin: 10% auto;
        padding: 20px;
        width: 95%;
    }
}

@media (max-width: 480px) {
    .ppc-metrics-grid,
    .traffic-metrics-grid {
        grid-template-columns: 1fr;
    }
    
    .dashboard-title {
        font-size: 1.5rem;
    }
    
    .executive-summary {
        padding: 20px;
    }
    
    .metric-card {
        padding: 20px;
    }
    
    .brand-card,
    .objective-card {
        padding: 20px;
    }
}

/* Print Styles */
@media print {
    .tab-navigation {
        display: none;
    }
    
    .tab-content {
        display: block !important;
        page-break-inside: avoid;
        margin-bottom: 30px;
    }
    
    .dashboard-header {
        background: #1e3a8a !important;
        -webkit-print-color-adjust: exact;
    }
    
    .brand-card,
    .metric-card,
    .objective-card {
        box-shadow: none;
        border: 1px solid #e5e7eb;
    }
}

/* Loading Animation */
@keyframes countUp {
    from { opacity: 0; }
    to { opacity: 1; }
}

.metric-value[data-target] {
    animation: countUp 0.5s ease-out;
}'''

# Save the CSS file
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ Created style.css")