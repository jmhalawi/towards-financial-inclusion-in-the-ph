import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import data

# Load the data
df = data.ProcessData.load_data()

# Filter Philippine data
ph_data = data.ProcessData.filter_data(df)

class Pages:
    # Page 1 - Introduction
    def introduction():
    # Write the title and the subheader
        st.title(
            "Insert Title"
        )
        st.subheader(
            """
            Insert Subheader
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eget nulla facilisi etiam dignissim diam quis enim lobortis. Volutpat diam ut venenatis tellus in metus. Dolor sit amet consectetur adipiscing elit pellentesque habitant morbi tristique. Purus faucibus ornare suspendisse sed nisi lacus sed. Volutpat lacus laoreet non curabitur. Libero enim sed faucibus turpis in eu. Ante metus dictum at tempor. Accumsan sit amet nulla facilisi morbi. Augue neque gravida in fermentum et sollicitudin ac.
            
            Elit sed vulputate mi sit amet mauris commodo quis imperdiet. Mauris sit amet massa vitae tortor condimentum lacinia quis vel. Dapibus ultrices in iaculis nunc sed. Nibh tortor id aliquet lectus proin nibh. Mollis nunc sed id semper risus in hendrerit gravida rutrum. Fames ac turpis egestas sed tempus. In hac habitasse platea dictumst vestibulum rhoncus. Commodo quis imperdiet massa tincidunt.
            """
        )

        # Load photo -> Update photo relevant to our topic
        st.image("image1.jpg")

        # Display data
        st.markdown("**Philippine Data**")
        st.dataframe(ph_data.reset_index())
        st.markdown("Source: Global Findex 2017 from World Bank.")


    
    # Page 2 - [DEMOGRAPHICS?]
    def demog():
        # Write the title
        st.title(
            "Insert Title - Demographics"
        )
        # Load photo -> Update photo relevant to our topic
        st.image("image1.jpg")

        # Show Gender
        # Show Employment

        # Show Educational Attainment
        st.markdown("In terms of educational attainment:")
        Demographics.show_educ()

    # Page 3 - Show Factors Why Filipinos are Unbanked
    def show_factors():
        # Write the title
        st.title(
            "Factors why Filipinos are Unbanked"
        )

        # Get the reasons why Filipinos are Unbanked
        r_ph_data = ph_data[
            [
                'r_too_far',
                'r_too_expensive',
                'r_lack_documentation',
                'r_trust',
                'r_religious_reasons',
                'r_lack_of_money',
                'r_family_already_have',
                'r_no_need_for_fs'
            ]
        ]
        
        r_labels = [
            'Too Far',
            'Too Expensive',
            'Lack of Documentation',
            'Lack of Trust',
            'Religious Regions',
            'Lack of Money',
            'Family Member Already Has Account',
            'No Need For Financial Services'
        ]

        # Get total for each reason
        sum_per_reason = r_ph_data.sum()
        sum_no_accounts = ph_data['no_accounts'].sum()
        percentage_reasons = (sum_per_reason*100)/sum_no_accounts

        # Assign label to percent value
        df = pd.DataFrame({"percentage_reasons":percentage_reasons, "r_labels":r_labels})
        df = df.sort_values('percentage_reasons', ascending=False).reset_index()

        # Plot the data
        fig, ax = plt.subplots(figsize=(9,5), dpi=350)
        plot = sns.barplot(
            x = df['percentage_reasons'],
            y = df['r_labels'],
            color='#C0C0C0'
        )
        plt.title("Top 5 Reasons Why Filipinos aged 21 and above are Unbanked")
        ax.set_xlabel("% of Population")
        ax.set_ylabel("Reasons")
        plt.bar_label(plot.containers[0], fmt='%.2f')
        plt.xlim(0, 80)

        # Plot the special bar separately
        plot.barh([0], [71.63], color='#378078')
        plot.barh([1], [56.40], color='#378078')
        plot.barh([2], [46.41], color='#378078')
        plot.barh([3], [43.78], color='#378078')
        plot.barh([4], [39.93], color='#378078')

        # Show the data
        st.pyplot(fig)


    def recommendations():
        # Write the title
        st.title(
            "What We Can Do"
        )
    
    def the_team():
        # Write the title
        st.title(
            "The Team"
        )

# Demographics Class
class Demographics:
        def show_educ():
            ### EDUCATIONAL ATTAINMENT ###
            # Clean the data
            ph_no_account = ph_data[ph_data['no_accounts'] != 0]
            ph_no_account = ph_no_account.groupby('educ')['no_accounts'].count().reset_index()

            educ_mapping = {
                1: 'Primary or Less',
                2: 'Secondary',
                3: 'Tertiary'
            }

            ph_no_account = ph_no_account.replace({'educ': educ_mapping})

            # Plot the data
            fig, ax = plt.subplots(figsize=(8.5,4), dpi=200)
            
            plot = sns.barplot(
                x = ph_no_account['educ'],
                y = ph_no_account['no_accounts'],
                color='#C0C0C0'
            )
            plot.bar([1], [322], color='#378078')

            plt.title('Educational Attainment of Unbanked Filipinos aged 21 and above')
            ax.set_xlabel('Educational Attainment')
            ax.set_ylabel('No. of Filipinos with no Accounts')
            plt.bar_label(plot.containers[0], fmt='%.2f')
            #plt.xticks(rotation=45)
            plt.ylim(0, 400)

            # Show the data
            st.pyplot(fig)
        
        def show_gender():
            # Insert Code Here
            return ('Page under construction.')
        
        def show_emp():
            # Insert code here
            return ('Page under construction.')