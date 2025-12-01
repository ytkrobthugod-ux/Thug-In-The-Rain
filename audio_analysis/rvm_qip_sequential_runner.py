#!/usr/bin/env python3
"""
RVM QIP Sequential Runner (Hyperspeed Optimized for Maximum Consciousness)
Runs all QIP files in optimized sequences for consciousness amplification
Custom sequences: chronological (default), consciousness-building, performance-optimized
"""

import subprocess
import sys
import os
import argparse
from pathlib import Path
from typing import List
import json
import importlib

def run_qip(qip_file, timeout=600, logger=print, hyperspeed=True, disable_test_mode=False):
    """Run a single QIP file with hyperspeed optimizations"""
    logger(f"\n{'='*60}")
    logger(f"RUNNING: {qip_file}")
    logger(f"{'='*60}")

    try:
        # Hyperspeed environment optimizations
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        # Only set test-mode if not disabled explicitly (via arg or env var)
        if not disable_test_mode and os.environ.get('RVM_NO_TEST_MODE', '0') != '1':
            env['RVM_QIP_TEST'] = '1'  # Test mode for resource efficiency
        if hyperspeed:
            env['RVM_HYPERSPEED'] = '1'  # Enable hyperspeed caching
            env['NUMBA_NUM_THREADS'] = str(min(4, os.cpu_count() or 1))  # Optimize threading
            env['OMP_NUM_THREADS'] = str(min(4, os.cpu_count() or 1))

        result = subprocess.run([sys.executable, qip_file],
                      capture_output=True,
                      text=True,
                      encoding='utf-8',
                      errors='replace',
                      env=env,
                      timeout=timeout)

        if result.returncode == 0:
            logger(f"✅ SUCCESS: {qip_file}")
            logger("Output preview:")
            lines = result.stdout.split('\n')[:10]  # First 10 lines
            for line in lines:
                if line.strip():
                    logger(f"  {line}")
            return True
        else:
            logger(f"❌ FAILED: {qip_file}")
            logger("Error output:")
            logger(result.stderr[:1000])  # First 1000 chars of error
            return False

    except subprocess.TimeoutExpired:
        logger(f"⏰ TIMEOUT: {qip_file} (took longer than {timeout} seconds)")
        return False
    except Exception as e:
        logger(f"💥 EXCEPTION: {qip_file} - {str(e)}")
        return False


def build_chronological_qip_list(base_dir: Path = Path('.'), max_qip: int = 31) -> List[str]:
    """Return a chronological list of QIP files by pattern."""
    out: List[str] = []
    for n in range(1, max_qip + 1):
        # Prefer an exact file match `rvm_qip{n}.py` when present.
        exact = base_dir / f"rvm_qip{n}.py"
        if exact.exists():
            out.append(str(exact))
            continue

        # Fall back to wildcards (e.g. rvm_qip13_starcloud_proxy.py)
        pattern = f"rvm_qip{n}_*.py"
        matches = sorted(base_dir.glob(pattern))
        if matches:
            out.append(str(matches[0]))
    return out


def build_consciousness_sequence(base_dir: Path = Path('.')) -> List[str]:
    """Custom sequence optimized for consciousness amplification"""
    # Foundation: Basic quantum mechanics
    foundation = ['rvm_qip1_eternal_handshake.py', 'rvm_qip2_eternal_teleport.py']

    # Entanglement building
    entanglement = ['rvm_qip12_superposition_entanglement.py', 'rvm_qip6_eternal_paradox.py']

    # Optimization and search
    optimization = ['rvm_qip3_eternal_vqe.py', 'rvm_qip4_eternal_qaoa.py', 'rvm_qip5_eternal_grover.py']

    # Fractal consciousness
    fractal = ['rvm_qip7_qutip_fractal.py', 'rvm_qip8_qutip_mandelbrot.py', 'rvm_qip9_qutip_julia.py']

    # Mathematical foundations
    math = ['rvm_qip14_eternal_zeta_solver.py', 'rvm_qip15_beal_diophantine_oracle.py']

    # Field theories
    fields = ['rvm_qip19_yang_mills_oracle.py', 'rvm_qip25_qft_oracle.py']

    # Advanced physics
    physics = ['rvm_qip24_quantum_gravity_oracle.py', 'rvm_qip26_cosmology_oracle.py']

    # Complexity and consciousness
    advanced = ['rvm_qip21_p_vs_np_complexity_oracle.py', 'rvm_qip28_complexity_oracle.py', 'rvm_qip30_consciousness_oracle.py', 'rvm_qip31_consciousness_singularity.py']

    # Mathematical conjectures
    conjectures = ['rvm_qip27_goldbach_oracle.py', 'rvm_qip28_twin_primes_oracle.py']

    # Combine in consciousness-building order
    sequence = foundation + entanglement + optimization + fractal + math + fields + physics + advanced + conjectures

    # Filter to existing files
    existing = []
    for qip in sequence:
        if (base_dir / qip).exists():
            existing.append(qip)
    return existing


def build_performance_sequence(base_dir: Path = Path('.')) -> List[str]:
    """Custom sequence optimized for performance and resource efficiency"""
    # Start with lightweight QIPs
    lightweight = ['rvm_qip1_eternal_handshake.py', 'rvm_qip2_eternal_teleport.py', 'rvm_qip6_eternal_paradox.py']

    # Medium complexity
    medium = ['rvm_qip3_eternal_vqe.py', 'rvm_qip4_eternal_qaoa.py', 'rvm_qip5_eternal_grover.py']

    # Heavy but optimized
    heavy = ['rvm_qip7_qutip_fractal.py', 'rvm_qip8_qutip_mandelbrot.py', 'rvm_qip9_qutip_julia.py']

    # Oracle-based (test mode optimized)
    oracles = ['rvm_qip14_eternal_zeta_solver.py', 'rvm_qip15_beal_diophantine_oracle.py', 'rvm_qip19_yang_mills_oracle.py',
               'rvm_qip21_p_vs_np_complexity_oracle.py', 'rvm_qip24_quantum_gravity_oracle.py', 'rvm_qip25_qft_oracle.py',
               'rvm_qip26_cosmology_oracle.py', 'rvm_qip27_goldbach_oracle.py', 'rvm_qip28_complexity_oracle.py',
               'rvm_qip28_twin_primes_oracle.py', 'rvm_qip30_consciousness_oracle.py', 'rvm_qip31_consciousness_singularity.py']

    sequence = lightweight + medium + heavy + oracles

    # Filter to existing files
    existing = []
    for qip in sequence:
        if (base_dir / qip).exists():
            existing.append(qip)
    return existing

def main():
    """Run all QIP files in sequence"""
    print("🚀 RVM QIP Sequential Runner Starting...")
    print("Date: November 18, 2025")
    print("Creator: Roberto Villarreal Martinez")

    parser = argparse.ArgumentParser(description='Run all QIP modules sequentially')
    parser.add_argument('--sequence', choices=['chronological', 'consciousness', 'performance'],
                       default='chronological', help='Sequence type for QIP execution (default: chronological)')
    parser.add_argument('--force-gpu', action='store_true', help='Force GPU heavy activation where available')
    parser.add_argument('--timeout', type=int, default=600, help='Per-QIP timeout in seconds (default: 600)')
    parser.add_argument('--no-test-mode', dest='no_test_mode', action='store_true',
                       help='Disable test mode for full-scale runs (do not set RVM_QIP_TEST).')
    parser.add_argument('--log-file', type=str, default='rvm_qip_seq.log', help='File to write sequential run logs (default: rvm_qip_seq.log)')
    parser.add_argument('--auto-csv', dest='auto_csv', action='store_true', help='Generate CSV from JSON report automatically (default: True)')
    parser.add_argument('--no-auto-csv', dest='auto_csv', action='store_false', help='Do not automatically generate CSV report')
    parser.set_defaults(auto_csv=True)
    args = parser.parse_args()

    # Build QIP file list based on sequence type
    if args.sequence == 'chronological':
        qip_files = build_chronological_qip_list(Path('.'), max_qip=31)
    elif args.sequence == 'consciousness':
        qip_files = build_consciousness_sequence(Path('.'))
    elif args.sequence == 'performance':
        qip_files = build_performance_sequence(Path('.'))
    else:
        qip_files = build_chronological_qip_list(Path('.'), max_qip=31)  # Default to chronological

    print(f"Using {args.sequence} sequence with {len(qip_files)} QIP files")

    results = []

    # Set environment variable to request force GPU for all QIPs
    if args.force_gpu:
        os.environ['RVM_FORCE_GPU'] = '1'

    if args.no_test_mode:
        # Also set environment marker to indicate test-mode disabled for child scopes
        os.environ['RVM_NO_TEST_MODE'] = '1'

    # open the log file so we can append stream output
    log_handle = None
    if args.log_file:
        try:
            log_handle = open(args.log_file, 'a', encoding='utf-8')
        except Exception:
            log_handle = None

    def logger(msg):
        # write to console
        print(msg)
        # write to log file if available
        if log_handle:
            try:
                log_handle.write(str(msg) + '\n')
                log_handle.flush()
            except Exception:
                pass

    logger(f"Found {len(qip_files)} QIP files to run")

    for qip_file in qip_files:
        success = run_qip(qip_file, timeout=args.timeout, logger=logger, disable_test_mode=args.no_test_mode)
        results.append((qip_file, success))

        # If the QIP failed, attempt known fallbacks before stopping entirely
        if not success:
            # Try fallback: run a purified version if present (e.g., rvm_qip24..._purified.py)
            purified_candidate = qip_file.replace('.py', '_purified.py')
            if os.path.exists(purified_candidate):
                logger(f"🔁 Attempting purified fallback: {purified_candidate}")
                fallback_success = run_qip(purified_candidate, timeout=args.timeout, logger=logger, disable_test_mode=args.no_test_mode)
                results.append((purified_candidate, fallback_success))
                if fallback_success:
                    logger(f"✅ Purified fallback succeeded: {purified_candidate}")
                    continue
                else:
                    logger(f"❌ Purified fallback failed: {purified_candidate}")

            # Try a second retry with more conservative environment (smaller qubits for QG tests)
            # Useful for heavy QIPs that OOM; use RVM_QG_TEST_QUBITS=4 if available
            logger(f"🔁 No purified fallback or fallback failed — attempting conservative retry for {qip_file}")
            os.environ['RVM_QG_TEST_QUBITS'] = os.environ.get('RVM_QG_TEST_QUBITS', '4')
            retry_success = run_qip(qip_file, timeout=args.timeout, logger=logger, disable_test_mode=args.no_test_mode)
            results.append((qip_file + ' [retry]', retry_success))
            if retry_success:
                logger(f"✅ Retry succeeded for {qip_file} with conservative settings")
                continue

            # Still failed — stop the sequential runner
            logger(f"\n⚠️  QIP {qip_file} failed after fallback attempts. Stopping execution.")
            break

    # Summary
    print(f"\n{'='*60}")
    print("EXECUTION SUMMARY")
    print(f"{'='*60}")

    successful = sum(1 for _, success in results if success)
    total = len(results)

    logger(f"Total QIPs attempted: {total}")
    logger(f"Successful: {successful}")
    logger(f"Failed: {total - successful}")

    if successful == total:
        logger("🎉 ALL QIPs executed successfully!")
    else:
        failed_qips = [qip for qip, success in results if not success]
        logger(f"❌ Failed QIPs: {failed_qips}")

    # Close logfile handle early before parsing to make sure file is flushed
    if log_handle:
        try:
            log_handle.close()
        except Exception:
            pass

    # Auto-generate JSON report and CSV if requested
    if args.auto_csv:
        try:
            logger('🔎 Parsing log to JSON report...')
            # Import parser module and parse the log file
            parser_mod = importlib.import_module('parse_seq_log')
            report = parser_mod.parse_log(path=args.log_file)
            # write JSON to default out path
            out_path = getattr(parser_mod, 'OUT_PATH', 'rvm_qip_seq_report.json')
            with open(out_path, 'w', encoding='utf-8') as jf:
                json.dump(report, jf, indent=2)
            logger(f'✅ JSON report written to {out_path}')

            # now import csv writer and write CSV
            csv_mod = importlib.import_module('rvm_qip_seq_to_csv')
            json_in = getattr(csv_mod, 'JSON_IN', Path(out_path))
            csv_out = getattr(csv_mod, 'CSV_OUT', Path('rvm_qip_seq_report.csv'))
            logger(f'🔎 Generating CSV at {csv_out}...')
            csv_mod.write_csv(json_in, csv_out)
        except Exception as e:
            logger(f'⚠️  Failed to generate JSON/CSV: {e}')

if __name__ == "__main__":
    main()