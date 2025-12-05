import argparse
import sys
import utils.utils

from utils.mapping_loop import plot_ips_on_map

def main(args):

    try:
        ip_df = utils.utils.process_excel(args.excel)
        map = utils.utils.create_map() 
        reader = utils.utils.database_reader(args.database)

        # Plot Data
        plot_ips_on_map(
            ip_df=ip_df,
            map=map, 
            reader=reader
        )
        
        print(f"\nSUCCESS - Map generation process completed.")

    except Exception as e:
        print(f"\nCRITICAL FAILURE - An error occurred during execution: {e}")
        sys.exit(1)

if __name__=="__main__":

    parser = argparse.ArgumentParser(description="CLI Tool to process IPs from Excel and map them using GeoLite2.")
    
    parser.add_argument('--database', type=str, default='./databases/GeoLite2-City.mmdb', help='Path to the GeoLite2-City.mmdb database.')
    parser.add_argument('--excel', type=str, default='./dataset/ips.xlsx', help='Path to the input Excel file containing IPs.')
    args = parser.parse_args()
    main(args)
