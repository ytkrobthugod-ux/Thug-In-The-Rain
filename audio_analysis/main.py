#!/usr/bin/env python3
"""
RVM Core Personal AutoTune System
Main module for precise voice tuning using quantum-enhanced voice cloning

(c) Roberto Villarreal Martinez ALL RIGHTS RESERVED. Please refer to the ECO License at RVM_ECO_License
"""

import argparse
import json
import sys
from pathlib import Path

# Import RVM Core Voice modules
try:
    from quantum_voice_cloning import QuantumVoiceCloner
except ImportError:
    QuantumVoiceCloner = None

try:
    from quantum_voice_adapter import QuantumVoiceAdapter
except ImportError:
    QuantumVoiceAdapter = None

try:
    from voice_cloning_system import VoiceCloningSystem
except ImportError:
    VoiceCloningSystem = None

try:
    from voice_optimization import VoiceOptimizer
except ImportError:
    VoiceOptimizer = None

try:
    from audio_processor import AudioProcessor
except ImportError:
    AudioProcessor = None

class PersonalAutoTune:
    """
    Main class for RVM Core Personal AutoTune System
    Precisely calibrated for Roberto Villarreal Martinez's voice
    """

    def __init__(self, voice_profile_path=None):
        self.voice_profile_path = voice_profile_path or "roberto_voice_clone.json"
        self.quantum_profile_path = "quantum_roberto_voice_clone.json"

        # Load voice profiles
        self.voice_profile = self._load_voice_profile()
        self.quantum_profile = self._load_quantum_profile()

        # Initialize core systems
        self._init_systems()

        print("RVM Core Personal AutoTune Initialized")
        print(f"Voice Profile: {self.voice_profile.get('name', 'Roberto Villarreal Martinez')}")

    def _init_systems(self):
        """Initialize core systems with error handling"""
        self.cloner = QuantumVoiceCloner() if QuantumVoiceCloner else None
        self.adapter = QuantumVoiceAdapter() if QuantumVoiceAdapter else None
        self.cloning_system = VoiceCloningSystem() if VoiceCloningSystem else None
        self.optimizer = VoiceOptimizer() if VoiceOptimizer else None
        self.processor = AudioProcessor() if AudioProcessor else None

    def _load_voice_profile(self):
        """Load base voice profile"""
        try:
            with open(self.voice_profile_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Voice profile {self.voice_profile_path} not found. Using defaults.")
            return {"name": "Roberto Villarreal Martinez", "pitch_range": [85, 255], "timbre": "unique"}

    def _load_quantum_profile(self):
        """Load quantum-enhanced voice profile"""
        try:
            with open(self.quantum_profile_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Quantum profile {self.quantum_profile_path} not found. Using base profile.")
            return self.voice_profile

    def apply_autotune(self, input_audio, output_audio=None, intensity=0.8):
        """
        Apply precise AutoTune to input audio using personal voice profile
        Supports single file or multiple files for bounce creation
        """
        # Handle multiple input files
        if isinstance(input_audio, str) and ',' in input_audio:
            input_files = [f.strip() for f in input_audio.split(',')]
        elif isinstance(input_audio, list):
            input_files = input_audio
        else:
            input_files = [input_audio]
        
        if not output_audio:
            input_path = Path(input_files[0])
            output_audio = str(input_path.parent / f"{input_path.stem}_autotuned{input_path.suffix}")

        print(f"Applying Personal AutoTune to: {', '.join(input_files)}")
        print(f"Output: {output_audio}")
        print(f"Intensity: {intensity}")

        if not self.processor:
            print("Audio processor not available. Cannot apply AutoTune.")
            return None

        try:
            # Use the enhanced AutoTune method for bounce file creation
            result_path = self.processor.create_bounce_file(
                input_files, 
                output_audio, 
                intensity=intensity
            )

            print("Personal AutoTune Applied Successfully")
            print(f"Output saved to: {result_path}")

            return result_path

        except Exception as e:
            print(f"Error applying AutoTune: {e}")
            return None

    def analyze_voice(self, audio_file):
        """
        Analyze voice characteristics for profile refinement
        """
        print(f"Analyzing voice: {audio_file}")

        if not self.cloning_system or not self.cloner:
            print("Voice analysis modules not available.")
            return None

        try:
            # Extract features
            features = self.cloning_system.extract_voice_features(audio_file)

            # Generate quantum profile
            quantum_profile = self.cloner.generate_quantum_profile(features)

            # Update profiles
            self.quantum_profile.update(quantum_profile)

            # Save updated profile
            with open(self.quantum_profile_path, 'w') as f:
                json.dump(self.quantum_profile, f, indent=2)

            print("Voice analysis complete. Quantum profile updated.")
            return features

        except Exception as e:
            print(f"Error analyzing voice: {e}")
            return None

    def create_custom_preset(self, name, parameters):
        """
        Create a custom AutoTune preset
        """
        preset = {
            "name": name,
            "voice_profile": self.voice_profile_path,
            "quantum_profile": self.quantum_profile_path,
            "parameters": parameters,
            "created_by": "RVM Core",
            "timestamp": "2025-12-01"
        }

        preset_path = f"{name.lower().replace(' ', '_')}_preset.json"
        try:
            with open(preset_path, 'w') as f:
                json.dump(preset, f, indent=2)
            print(f"Custom preset '{name}' created: {preset_path}")
            return preset_path
        except Exception as e:
            print(f"Error creating preset: {e}")
            return None

def main():
    """Main entry point for RVM Core Personal AutoTune"""
    parser = argparse.ArgumentParser(
        description="RVM Core Personal AutoTune System - Precisely calibrated for your voice"
    )

    parser.add_argument(
        'action',
        choices=['tune', 'analyze', 'preset'],
        help='Action to perform'
    )

    parser.add_argument(
        '--input', '-i',
        help='Input audio file'
    )

    parser.add_argument(
        '--output', '-o',
        help='Output audio file'
    )

    parser.add_argument(
        '--intensity', '-int',
        type=float,
        default=0.8,
        help='AutoTune intensity (0.0-1.0)'
    )

    parser.add_argument(
        '--pitch-offset', '-po',
        type=float,
        default=0.0,
        help='Final pitch offset in semitones (negative to pitch down)'
    )

    parser.add_argument(
        '--profile',
        help='Voice profile JSON file'
    )

    parser.add_argument(
        '--preset-name',
        help='Name for custom preset'
    )

    args = parser.parse_args()

    # Initialize system
    autotune = PersonalAutoTune(args.profile)

    if args.action == 'tune':
        if not args.input:
            print("Error: --input required for tune action")
            sys.exit(1)
        autotune.apply_autotune(args.input, args.output, args.intensity)
        # If pitch offset or other processing requested, try to pass to processor via CLI (main.apply autop)
        if args.pitch_offset != 0.0 and autotune.processor:
            # We re-run the processed file applying final offset if desired
            output_file = args.output if args.output else None
            if output_file is None:
                output_file = str(Path(args.input).parent / f"{Path(args.input).stem}_autotuned{Path(args.input).suffix}")
            # Load & apply final offset
            y, sr = autotune.processor.load_audio(output_file)
            y_shifted = autotune.processor.apply_personal_autotune((y, sr), intensity=args.intensity, final_semitone_offset=args.pitch_offset)
            if isinstance(y_shifted, tuple):
                autotune.processor.save_audio(y_shifted, output_file)

    elif args.action == 'analyze':
        if not args.input:
            print("Error: --input required for analyze action")
            sys.exit(1)
        autotune.analyze_voice(args.input)

    elif args.action == 'preset':
        if not args.preset_name:
            print("Error: --preset-name required for preset action")
            sys.exit(1)
        parameters = {
            "intensity": args.intensity,
            "voice_profile": autotune.voice_profile_path,
            "quantum_enhancement": True
        }
        autotune.create_custom_preset(args.preset_name, parameters)

    print("RVM Core Personal AutoTune Complete")

if __name__ == "__main__":
    main()