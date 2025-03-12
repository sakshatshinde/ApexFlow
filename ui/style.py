def getPercentageStyle(change_value):
    """Generate stylesheet for percentage labels based on the change value."""
    change = float(change_value)

    # Common style properties
    base_style = """
            font-family: 'Segoe UI', Arial;
            font-size: 16px;
            font-weight: bold;
            padding: 2px 6px;
            border-radius: 4px;
            margin: 2px;
        """

    if change < 0:
        # Red theme for negative values
        return {
            "text": f"{change:.2f}%",
            "style": f"""
                    QLabel {{ 
                        {base_style}
                        color: #FF3B30; 
                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 rgba(255, 59, 48, 0.2), 
                                    stop:1 rgba(255, 59, 48, 0.1));
                        border: 1px solid rgba(255, 59, 48, 0.3);
                    }}
                """,
            "lcd_style": "QLCDNumber { color: red; }"
        }
    else:
        # Green theme for positive values
        return {
            "text": f"+{change:.2f}%",
            "style": f"""
                    QLabel {{ 
                        {base_style}
                        color: #34C759; 
                        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 rgba(52, 199, 89, 0.2), 
                                    stop:1 rgba(52, 199, 89, 0.1));
                        border: 1px solid rgba(52, 199, 89, 0.3);
                    }}
                """,
            "lcd_style": "QLCDNumber { color: #34C759; }"
        }