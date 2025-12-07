import { motion } from "framer-motion"
import { PROFILE } from "@/data/profile"
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

export const Experience = () => {
    return (
        <section id="experience" className="py-20 scroll-mt-16">
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5 }}
                className="space-y-8"
            >
                <h2 className="text-3xl font-bold tracking-tight">Professional Experience</h2>

                <div className="space-y-6">
                    {PROFILE.experience.map((exp, index) => (
                        <Card key={index} className="overflow-hidden">
                            <div className="md:flex">
                                <div className="bg-muted p-6 md:w-64 flex flex-col justify-center">
                                    <span className="text-sm font-semibold text-primary mb-1">{exp.period}</span>
                                    <h3 className="font-bold text-lg">{exp.company}</h3>
                                </div>
                                <div className="p-6 flex-1">
                                    <h4 className="text-xl font-semibold mb-2">{exp.role}</h4>
                                    <p className="text-muted-foreground mb-4">{exp.description}</p>
                                    <ul className="space-y-2 list-disc pl-5 text-sm text-muted-foreground">
                                        {exp.achievements.map((item, i) => (
                                            <li key={i}>{item}</li>
                                        ))}
                                    </ul>
                                </div>
                            </div>
                        </Card>
                    ))}
                </div>
            </motion.div>
        </section>
    )
}
