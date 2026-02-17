import json
import argparse
import logging
import socket
from Bio.PDB.MMCIFParser import MMCIFParser

CIF_FILE = '4HHB.cif'
OUTPUT_JSON = 'output_files/4HHB_summary.json'


parser = argparse.ArgumentParser()
parser.add_argument(
    '-l', '--loglevel',
    type=str,
    required=False,
    default='WARNING',
    help='set log level to DEBUG, INFO, WARNING, ERROR, or CRITICAL'
)
args = parser.parse_args()

format_str = (
    f'[%(asctime)s {socket.gethostname()}] '
    '%(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
)
logging.basicConfig(level=args.loglevel, format=format_str)



def summarize_chain(chain: object) -> dict:
    """
    Summarize residue statistics for a single chain.

    Args:
        chain (object): Biopython Chain object.

    Returns:
        dict: Per-chain summary containing chain_id, total_residues,
              standard_residues, and hetero_residue_count.
    """
    chain_id = chain.get_id()
    total_residues = 0
    standard_residues = 0
    hetero_residue_count = 0

    logging.debug(f"Summarizing chain {chain_id}")

    for residue in chain:
        total_residues += 1
        hetfield, resseq, icode = residue.get_id()

        if hetfield == ' ':
            standard_residues += 1
        else:
            hetero_residue_count += 1

    return {
        "chain_id": chain_id,
        "total_residues": total_residues,
        "standard_residues": standard_residues,
        "hetero_residue_count": hetero_residue_count
    }


def summarize_mmcif_file(cif_file: str) -> dict:
    """
    Parse an mmCIF file and compute per-chain residue statistics
    for the first model only.

    Args:
        cif_file (str): Path to mmCIF file.

    Returns:
        dict: Top-level dictionary with key "chains" containing
              a list of per-chain summary dictionaries.
    """
    logging.info(f"Parsing mmCIF file {cif_file}")

    parser = MMCIFParser()

    with open(cif_file, 'r') as f:
        structure = parser.get_structure('structure', f)

    models = list(structure)

    if len(models) == 0:
        logging.warning("No models found in structure")
        return {"chains": []}

    model = models[0]
    chains_summary = []

    for chain in model:
        chains_summary.append(summarize_chain(chain))

    logging.info(f"Finished summarizing {len(chains_summary)} chains")

    return {"chains": chains_summary}


def write_summary_to_json(summary: dict, output_file: str) -> None:
    """
    Write summary dictionary to a JSON file.

    Args:
        summary (dict): Summary data.
        output_file (str): Output JSON file path.

    Returns:
        None
    """
    logging.info(f"Writing summary to {output_file}")

    with open(output_file, 'w') as outfile:
        json.dump(summary, outfile, indent=2)

    logging.info(f"Finished writing {output_file}")


def main() -> None:
    """
    Run the mmCIF summary workflow:
    1. Parse mmCIF file
    2. Compute per-chain residue statistics
    3. Write results to JSON file

    Args:
        None

    Returns:
        None
    """
    logging.info("Starting mmCIF summary workflow")

    try:
        summary = summarize_mmcif_file(CIF_FILE)
        write_summary_to_json(summary, OUTPUT_JSON)

    except FileNotFoundError:
        logging.error(f"Input file not found: {CIF_FILE}")
        raise

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise

    logging.info("mmCIF summary workflow complete")


if __name__ == '__main__':
    main()